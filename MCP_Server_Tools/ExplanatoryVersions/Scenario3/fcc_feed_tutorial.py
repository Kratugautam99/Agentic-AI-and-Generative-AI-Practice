# Tutorial: Creating an RSS Feed Reader with MCP
# This example shows how to create an MCP service that reads RSS feeds

# Step 1: Import required libraries
# We need FastMCP for creating the MCP service and feedparser for reading RSS feeds
from fastmcp import FastMCP
import feedparser

# Step 2: Create the MCP service
# Give it a descriptive name
mcp = FastMCP(name="FreeCodeCamp Content Explorer Tutorial")

# Step 3: Define a tool to search FreeCodeCamp's news feed
@mcp.tool()
def fcc_news_search(query: str, max_results: int = 3):
    """
    Search FreeCodeCamp's news feed for articles matching a query.
    
    This tool demonstrates how to:
    1. Parse an RSS feed
    2. Search through feed entries
    3. Return formatted results
    
    Args:
        query (str): The search term to look for in titles and descriptions
        max_results (int, optional): Maximum number of results to return. Defaults to 3.
    
    Returns:
        list: A list of dictionaries containing matching articles
    """
    # Step 3.1: Parse the RSS feed
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    
    # Step 3.2: Prepare for search
    results = []
    query_lower = query.lower()  # Convert to lowercase for case-insensitive search
    
    # Step 3.3: Search through entries
    for entry in feed.entries:
        # Get the title and description, using empty string as fallback
        title = entry.get("title", "")
        description = entry.get("description", "")
        
        # Check if query appears in title or description
        if query_lower in title.lower() or query_lower in description.lower():
            # Add matching article to results
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
            
            # Stop if we have enough results
            if len(results) >= max_results:
                break
    
    # Step 3.4: Return results or a "no results" message
    return results or [{"message": "No results found"}]

# Step 4: Define a tool to search FreeCodeCamp's YouTube channel
@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 3):
    """
    Search FreeCodeCamp's YouTube channel for videos matching a query.
    
    This tool demonstrates how to:
    1. Parse a YouTube RSS feed
    2. Search through video entries
    3. Return formatted results
    
    Args:
        query (str): The search term to look for in video titles
        max_results (int, optional): Maximum number of results to return. Defaults to 3.
    
    Returns:
        list: A list of dictionaries containing matching videos
    """
    # Step 4.1: Parse the YouTube RSS feed
    feed = feedparser.parse(
        "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    )
    
    # Step 4.2: Prepare for search
    results = []
    query_lower = query.lower()
    
    # Step 4.3: Search through entries
    for entry in feed.entries:
        title = entry.get("title", "")
        
        # Check if query appears in title
        if query_lower in title.lower():
            # Add matching video to results
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
            
            # Stop if we have enough results
            if len(results) >= max_results:
                break
    
    # Step 4.4: Return results or a "no results" message
    return results or [{"message": "No videos found"}]

# Step 5: Add a fun easter egg
@mcp.tool()
def fcc_secret_message():
    """
    Returns an inspirational message for learners.
    
    This demonstrates how to create a simple tool that returns a static value.
    """
    return "Keep exploring, keep learning, and happy coding! 🚀"

# Step 6: Run the service
if __name__ == "__main__":
    print("Starting the FreeCodeCamp Content Explorer...")
    print("This service allows you to:")
    print("1. Search FreeCodeCamp's news articles")
    print("2. Search FreeCodeCamp's YouTube videos")
    print("3. Get an inspirational message")
    mcp.run()  # Start the service using STDIO

# Try it out!
# Once running, you can:
# 1. Search for articles about "python"
# 2. Search for videos about "javascript"
# 3. Get the secret message