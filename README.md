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
   - Run the following command to download the reviews datasets using Kaggle API:
     ```bash
     kaggle datasets download -d snap/amazon-fine-food-reviews -p data/raw
     kaggle datasets download -d shivamparab/amazon-electronics-reviews -p data/raw
     kaggle datasets download -d yelp-dataset/yelp-dataset -p data/raw
     kaggle datasets download -d kazanova/sentiment140 -p data/raw
     kaggle datasets download -d lakshmi25npathi/imdb-dataset-of-50k-movie-reviews -p data/raw
     ```

2. **Extract the Dataset and Preprocess the Data**:
   - Run the following script to extract the data, label sentiments and clean the text:
     ```bash
     python -m src.data.preprocess
     ```

3. **Check the extracted files**:
  - After completing these steps, you should have the following preprocessed files in data/processed:
      - amazon_reviews_electronics_cleaned.csv
      - amazon_reviews_food_cleaned.csv
      - yelp_reviews_cleaned.csv
      - sentiment140_cleaned.csv
      - imdb_cleaned.csv