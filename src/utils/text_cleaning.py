import re
#import nltk
from nltk.corpus import stopwords


# Download stopwords if not already downloaded (uncomment if running for the first time)
# nltk.download('stopwords')

# Define stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Clean text by:
    - Converting to lowercase
    - Removing special characters and numbers
    - Removing stopwords
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Remove special characters and numbers using regex
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text