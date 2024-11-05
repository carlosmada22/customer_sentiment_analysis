# Customer Sentiment Analysis

## Folder Structure
- **data/**: Contains raw and processed datasets.
  - **raw/**: Original datasets.
  - **processed/**: Cleaned datasets ready for model training.
- **notebooks/**: Jupyter notebooks for data exploration.
- **src/**: Source code for data loading, preprocessing, and utility functions.
  - **data/**: Script for data preprocessing.
  - **utils/**: Scripts and functions for data cleaning.

## Getting Started

### Step 1: Download the Amazon Dataset

1. **Download the Dataset**: 
   - Run the following command to download the Amazon reviews dataset using Kaggle API:
     ```bash
     kaggle datasets download -d snap/amazon-fine-food-reviews -p data/raw
     ```

2. **Extract the Dataset and Preprocess the Data**:
   - Run the following script to extract the data, label sentiments and clean the text:
     ```bash
     python src/data/preprocess.py
     ```