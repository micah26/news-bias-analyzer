# src/news_fetcher.py - Core module for fetching news from NewsAPI
# This is a LIBRARY file - it provides functions that other files can use

import requests
import json
import sys
sys.path.append('..')
from config import NEWS_API_KEY, NEWS_API_BASE_URL


def fetch_news(topic, num_articles=5):
    """
    Fetch news articles about a specific topic from NewsAPI.
    
    This is a REUSABLE function that can be called from anywhere in the project.
    
    Parameters:
    -----------
    topic : str
        The topic to search for (e.g., "climate change", "technology")
    num_articles : int
        Maximum number of articles to fetch (default: 5)
    
    Returns:
    --------
    dict or None
        Dictionary containing news articles if successful, None if failed
    
    Example Usage:
    --------------
    from news_fetcher import fetch_news
    
    data = fetch_news("cricket", 10)
    if data:
        print(f"Found {len(data['articles'])} articles")
    """
    
    print(f"\n🔍 Searching for news about: '{topic}'")
    print(f"📊 Requesting up to {num_articles} articles...")
    
    endpoint = f"{NEWS_API_BASE_URL}/everything"
    
    params = {
        'q': topic,
        'pageSize': num_articles,
        'apiKey': NEWS_API_KEY,
        'language': 'en',
        'sortBy': 'publishedAt'
    }
    
    try:
        print("📡 Connecting to NewsAPI...")
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            print("✅ Successfully fetched news!\n")
            data = response.json()
            return data
        
        else:
            print(f"❌ Error: API returned status code {response.status_code}")
            print(f"Error message: {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error occurred: {e}")
        return None


def display_article_summary(article):
    """
    Display a nicely formatted summary of a single article.
    
    This is a REUSABLE function for displaying articles.
    
    Parameters:
    -----------
    article : dict
        A dictionary containing article data from NewsAPI
    """
    
    print("=" * 80)
    print(f"📰 TITLE: {article['title']}")
    print(f"📅 PUBLISHED: {article['publishedAt']}")
    print(f"🏢 SOURCE: {article['source']['name']}")
    print(f"✍️  AUTHOR: {article.get('author', 'Unknown')}")
    print(f"\n📝 DESCRIPTION:")
    print(f"   {article['description']}")
    print(f"\n🔗 URL: {article['url']}")
    print("=" * 80)
    print()


def get_article_sources(news_data):
    """
    Extract unique news sources from fetched data.
    
    Parameters:
    -----------
    news_data : dict
        News data returned from fetch_news()
    
    Returns:
    --------
    list
        List of unique source names
    """
    if not news_data or 'articles' not in news_data:
        return []
    
    sources = set()  # Use set to avoid duplicates
    for article in news_data['articles']:
        sources.add(article['source']['name'])
    
    return sorted(list(sources))  # Return sorted list


# ===== SIMPLE TEST SECTION =====
# This runs ONLY when you execute this file directly: python src/news_fetcher.py
# When other files IMPORT this file, this section is ignored

if __name__ == "__main__":
    print("=" * 80)
    print("🧪 TESTING news_fetcher.py Module")
    print("=" * 80)
    print("\nThis is a simple test to verify the module works.")
    print("For interactive testing, use: python src/interactive_searcher.py\n")
    
    # Simple test with a hard-coded topic
    test_topic = "technology"
    print(f"Testing with topic: '{test_topic}'\n")
    
    news_data = fetch_news(test_topic, num_articles=3)
    
    if news_data:
        print(f"✅ Module is working correctly!")
        print(f"   Total results: {news_data['totalResults']}")
        print(f"   Articles fetched: {len(news_data['articles'])}")
        print(f"   Sources: {', '.join(get_article_sources(news_data))}")
        
        print("\n📄 First article preview:")
        if news_data['articles']:
            display_article_summary(news_data['articles'][0])
    else:
        print("❌ Module test failed!")
    
    print("\n" + "=" * 80)
    print("✅ Test complete!")
    print("💡 TIP: For interactive search, run: python src/interactive_searcher.py")
    print("=" * 80)