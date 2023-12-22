
# Bug Severity Classification with RoBERTa

## Overview
This project uses the RoBERTa (Robustly Optimized BERT Pretraining Approach) model for classifying bug reports into different severity levels. The classification aims to distinguish between less severe bugs (trivial, minor, normal) and more severe bugs (major, critical, blocker).

## Requirements
- Python 3.x
- PyTorch
- Transformers library (Hugging Face)
- Pandas, Numpy, Scikit-Learn
- Matplotlib, Seaborn (for plotting)

## Data Preparation

For this project, we utilized the [Mozilla Dataset](https://github.com/ansymo/msr2013-bug_dataset), focusing on four major products: `Bugzilla, Core, Firefox, Thunderbird`. The dataset required for our analysis is in the format of a CSV file, comprising bug reports characterized by various fields such as `Bug_id,Timestamp,Assignee,Status,Components,os,Product,Resolution,Severity,Summary`. The `Severity` field categorizes bug reports into different levels, distinguishing between less severe and more severe bugs. We have divided this dataset into two parts: one for training and the other for testing purposes.

## Model
We use the [Roberta-base](https://huggingface.co/roberta-base) model from Hugging Face's transformers library. The model is fine-tuned for our binary classification task on the bug reports dataset.

## Training
The training process involves:
- Preprocessing and tokenizing the text data.
- Creating data loaders for handling training and testing data.
- Configuring the RoBERTa model and setting up the optimizer and scheduler.
- Training the model over multiple epochs and saving the model's state.

## Evaluation
The model's performance is evaluated using metrics like accuracy, precision, recall, F1 score, and ROC-AUC. Confusion matrices and loss plots are also generated for a comprehensive understanding of the model's performance.

## Usage
1. Raw dataset(Xml) and Final dataset(Csv)
2. Install all the required dependency.
2. Run the training script with the specified parameters.
3. Evaluate the model using the test dataset.
4. Use the trained model to classify new bug reports.

## File Structure
- `bug_severity_Roberta.ipynb`: Jupyter notebook containing the complete code for training and evaluating the model.
