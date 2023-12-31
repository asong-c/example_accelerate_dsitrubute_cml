import os
import datasets
from common import fine_tuner as common_ft
from peft import LoraConfig

cache_dir = common_ft.get_unique_cache_dir()

# The first X% of `train` split.
# With 2 V100 GPUs with the training options selected below, fine-tuning takes approximately 30 minutes
dataset_fraction = 100
data = datasets.load_dataset('philschmid/sql-create-context-copy', split=f'train[:{dataset_fraction}%]', cache_dir=cache_dir)

# Dataset modification function to merge multiple columns and add in some special tokens
def merge_columns(example):
    prediction_format = """<TABLE>: %s
<QUESTION>: %s
<SQL>: %s"""
    example["prediction"] = prediction_format%(example["context"], example["question"], example["answer"])
    return example


# Create prediction column with the format we want for the fine tuning
tuning_data = data.map(merge_columns)

# Load a model using PEFT library for finetuning
ft = common_ft.AMPFineTuner("bigscience/bloom-1b1")

# Set LoRA training configuration
ft.set_lora_config(
LoraConfig(
          r=16,
          lora_alpha=32,
          target_modules=["query_key_value", "xxx"],
          lora_dropout=0.05,
          bias="none",
          task_type="CAUSAL_LM"
      )
)

# Set training arguments 
# see fine_tuner.py for list of defaults and huggingface's transformers.TrainingArguments
# or the full list of arguments
ft.training_args.num_train_epochs=2
ft.training_args.warmup_ratio=0.03
ft.training_args.max_grad_norm=0.3
ft.training_args.learning_rate=2e-4

# Execute training and save adapter
ft.train(tuning_data, "prediction", os.getenv("/home/cdsw/adapters/bloom1b1-lora-sql")