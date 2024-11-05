import pandas as pd
import zipfile
from src.utils.text_cleaning import clean_text

def label_sentiment(score):
    """Labels sentiment based on the score."""
    if score <= 2:
        return 'negative'
    elif score == 3:
        return 'neutral'
    else:
        return 'positive'

def preprocess_amazon_data():
    """Loads, labels, cleans, and saves the Amazon reviews dataset."""

    with zipfile.ZipFile('data/raw/amazon-fine-food-reviews.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # Load the raw dataset
    data = pd.read_csv('data/raw/Reviews.csv')

    # Label the sentiment
    data['sentiment'] = data['Score'].apply(label_sentiment)

    # Clean the review text
    data['cleaned_text'] = data['Text'].apply(clean_text)

    # Save the processed data
    data[['cleaned_text', 'sentiment']].to_csv('data/processed/amazon_reviews_cleaned.csv', index=False)
    print("Amazon data has been preprocessed and saved to 'data/processed/amazon_reviews_cleaned.csv'")

if __name__ == "__main__":
    preprocess_amazon_data()