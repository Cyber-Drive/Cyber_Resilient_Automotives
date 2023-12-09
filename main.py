import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stopwords
nltk.download('punkt')
nltk.download('stopwords')


# Function to fetch articles (simulated with dummy URLs)
def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    return [article.get_text() for article in articles]


# Function to extract keywords from text
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words and word.isalpha()]
    freq_dist = nltk.FreqDist(filtered_text)
    return freq_dist.most_common(10)


# Example usage
url = "https://www.google.com/search?q=articles+on+blockchain+automotives&oq=articles+on+blockchain+automotives&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiiBBiJBdIBCDg4NzhqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8"  # Replace with actual URL
articles = fetch_articles(url)
print(articles)
for article in articles:
    print("Keywords:", extract_keywords(article))
