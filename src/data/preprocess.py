import pandas as pd
import zipfile
import json
from src.utils.text_cleaning import clean_text

def label_sentiment(score):
    """Labels sentiment based on the score."""
    if score >= 4:
        return 'positive'
    elif score == 3:
        return 'neutral'
    else:
        return 'negative'

def preprocess_amazon_food_data():
    """Loads, labels, cleans, and saves the Amazon reviews dataset."""

    with zipfile.ZipFile('data/raw/amazon-fine-food-reviews.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # Load the raw dataset
    data_food_amazon = pd.read_csv('data/raw/Reviews.csv')

    # Label the sentiment
    data_food_amazon['sentiment'] = data_food_amazon['Score'].apply(label_sentiment)

    # Clean the review text
    data_food_amazon['cleaned_text'] = data_food_amazon['Text'].apply(clean_text)

    # Save the processed data
    data_food_amazon[['cleaned_text', 'sentiment']].to_csv('data/processed/amazon_reviews_food_cleaned.csv', index=False)
    print("Amazon food data has been preprocessed and saved to 'data/processed/amazon_reviews_food_cleaned.csv'")

def preprocess_amazon_electronic_data():
    """Loads, labels, cleans, and saves the Amazon reviews dataset."""

    with zipfile.ZipFile('data/raw/amazon-electronics-reviews.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # Load the JSON file
    with open('data/raw/Electronics_5.json', 'r') as f:
        data = pd.DataFrame([json.loads(line) for line in f])

    # Label the sentiment
    data['sentiment'] = data['overall'].apply(label_sentiment)

    # Clean the review text
    data['cleaned_text'] = data['reviewText'].apply(clean_text)

    # Save the processed data
    data[['cleaned_text', 'sentiment']].to_csv('data/processed/amazon_reviews_electronics_cleaned.csv', index=False)
    print("Amazon electronics data has been preprocessed and saved to 'data/processed/amazon_reviews_electronic_cleaned.csv'")

def preprocess_yelp_data():
    """Loads, labels, cleans, and saves the Yelp reviews dataset."""

    with zipfile.ZipFile('data/raw/yelp-dataset.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # Load the Yelp dataset
    with open('data/raw/yelp_academic_dataset_review.json', 'r') as f:
        yelp_reviews = pd.DataFrame([json.loads(line) for line in f])

    # Label the sentiment
    yelp_reviews['sentiment'] = yelp_reviews['stars'].apply(label_sentiment)

    # Clean the review text
    yelp_reviews['cleaned_text'] = yelp_reviews['text'].apply(clean_text)

    # Save the processed data
    yelp_reviews[['cleaned_text', 'sentiment']].to_csv('data/processed/yelp_reviews_cleaned.csv', index=False)
    print("Yelp data has been preprocessed and saved to 'data/processed/yelp_reviews_cleaned.csv'")

def preprocess_tweet_data():
    """Loads, labels, cleans, and saves the Twitter sentiment tweets dataset."""

    with zipfile.ZipFile('data/raw/sentiment140.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # Load the Yelp dataset
    sentiment140 = pd.read_csv('data/raw/sentiment140.csv', encoding='ISO-8859-1', header=None)

    # Label the sentiment
    sentiment140['sentiment'] = sentiment140[0].apply(label_sentiment)

    # Clean the review text
    sentiment140['cleaned_text'] = sentiment140[5].apply(clean_text)

    # Save the processed data
    sentiment140[['cleaned_text', 'sentiment']].to_csv('data/processed/sentiment140_cleaned.csv', index=False)
    print("Twitter sentiment data has been preprocessed and saved to 'data/processed/sentiment140_cleaned.csv'")

def preprocess_imdb_data():
    """Loads, labels, cleans, and saves the Twitter sentiment tweets dataset."""

    with zipfile.ZipFile('data/raw/imdb-dataset-of-50k-movie-reviews.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw')

    # Load the Yelp dataset
    imdb = pd.read_csv('data/raw/IMDB_Dataset.csv')

    # Label the sentiment
    imdb['sentiment'] = imdb['sentiment']

    # Clean the review text
    imdb['cleaned_text'] = imdb['review'].apply(clean_text)

    # Save the processed data
    imdb[['cleaned_text', 'sentiment']].to_csv('data/processed/imdb_cleaned.csv', index=False)
    print("IMDB data has been preprocessed and saved to 'data/processed/imdb_cleaned.csv'")

if __name__ == "__main__":
    preprocess_amazon_food_data()
    preprocess_amazon_electronic_data()
    preprocess_yelp_data()
    preprocess_tweet_data()
    preprocess_imdb_data()