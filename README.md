# example_accelerate_distributed_amp_fine_tune_cml.ipynb
Notebook demonstrating accelerate in distributed mode across CML Workers with GPUs.

Using custom fine-tuning implementation using QLoRA and PEFT from to-be-released CML AMP.
## Requirements
### Runtime
JupyterLab - Python 3.9 - Nvidia GPU - 2023.05
- This uses huggingface libs for model and dataset download and requires git lfs support from this runtime or newer.
# example_accelerate_distributed_hf_cml.ipynb
Notebook demonstrating accelerate in distributed mode with CML Workers with GPUs.

Using the huggingface/accelerate sample nlp training script with accelerate and using CML Workers API to provision GPU sessions.
Training script runs in distributed mode accross the multiple CML workers.

## Requirements
### Runtime
JupyterLab - Python 3.9 - Nvidia GPU - 2023.05
- This uses huggingface libs for model and dataset download and requires git lfs support from this runtime or newer.

# example_local_fine_tune.ipynb
Notebook demonstrating QLoRA finetuning using hugginggface libs. Rune locally to the session with no distribution techniques.
## Requirements
### Runtime
JupyterLab - Python 3.9 - Nvidia GPU - 2023.05
- This uses huggingface libs for model and dataset download and requires git lfs support from this runtime or newer.

