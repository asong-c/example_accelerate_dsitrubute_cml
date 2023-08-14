# example_accelerate_dsitrubute_cml
Basic Notebook demonstrating accelerate in distributed mode with CML Workers with GPUs.

Using the huggingface/accelerate sample nlp training script with accelerate and using CML Workers API to provision GPU sessions.
Training script runs in distributed mode accross the multiple CML workers.

## Requirements
### Runtime
JupyterLab - Python 3.9 - Nvidia GPU - 2023.05
- This uses huggingface libs for model and dataset download and requires git lfs support from this runtime or newer.
