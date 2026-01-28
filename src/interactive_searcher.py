# src/interactive_searcher.py - Interactive command-line tool for testing news fetcher
# This is a TESTING TOOL - not part of the core project, just for development

import sys
sys.path.append('..')

# Import functions from our core module
from news_fetcher import fetch_news, display_article_summary, get_article_sources


def interactive_search():
    """
    Interactive news searcher - user enters topics and gets news.
    This is useful during development for testing different topics.
    """
    
    print("=" * 80)
    print("🎯 INTERACTIVE NEWS SEARCHER - Development Testing Tool")
    print("=" * 80)
    print("\nThis tool helps you test the news fetcher with different topics.")
    print("Type a topic to search for news, or 'quit' to exit.")
    print("\n💡 Try these examples:")
    print("   - 'climate change'")
    print("   - 'artificial intelligence'")
    print("   - 'cricket'")
    print("   - 'electric vehicles'\n")
    
    while True:
        # Get user input
        topic = input("🔍 Enter topic (or 'quit'): ").strip()
        
        # Check if user wants to quit
        if topic.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye! Happy coding!")
            break
        
        # Check if input is empty
        if not topic:
            print("⚠️  Please enter a topic!\n")
            continue
        
        # Ask how many articles
        try:
            num = input("📊 How many articles? (1-10, default 5): ").strip()
            num_articles = int(num) if num else 5
            
            # Validate range
            if num_articles < 1 or num_articles > 10:
                print("⚠️  Number must be between 1 and 10. Using 5.")
                num_articles = 5
        
        except ValueError:
            print("⚠️  Invalid number. Using 5.")
            num_articles = 5
        
        # Fetch news using our core module function
        news_data = fetch_news(topic, num_articles)
        
        if news_data and news_data['articles']:
            print(f"\n📊 RESULTS:")
            print(f"   Total results available: {news_data['totalResults']}")
            print(f"   Articles fetched: {len(news_data['articles'])}")
            
            # Show unique sources
            sources = get_article_sources(news_data)
            print(f"   Sources: {', '.join(sources)}")
            print()
            
            # Display each article
            for i, article in enumerate(news_data['articles'], 1):
                print(f"📄 ARTICLE #{i}")
                display_article_summary(article)
        
        else:
            print("❌ No articles found or error occurred.\n")
        
        print("\n" + "-" * 80 + "\n")


if __name__ == "__main__":
    interactive_search()