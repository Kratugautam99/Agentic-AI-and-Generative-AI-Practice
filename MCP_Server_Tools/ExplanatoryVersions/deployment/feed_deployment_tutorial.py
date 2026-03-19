# Tutorial: Deploying an MCP Service with HTTP Transport
# This example shows how to deploy an MCP service using HTTP transport

# Step 1: Import required libraries
from fastmcp import FastMCP
import feedparser

# Step 2: Create the MCP service
# Note: This is similar to our previous feed service, but configured for HTTP deployment
mcp = FastMCP(name="FreeCodeCamp Content Explorer (Deployed)")

# Step 3: Define the service tools
@mcp.tool()
def fcc_news_search(query: str, max_results: int = 3):
    """
    Search FreeCodeCamp's news feed via RSS by title/description.
    
    This tool is configured for HTTP deployment, making it accessible
    through a web interface.
    
    Args:
        query (str): The search term to look for
        max_results (int, optional): Maximum results to return. Defaults to 3.
    
    Returns:
        list: Matching articles or a "no results" message
    """
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
            
        if len(results) >= max_results:
            break
    
    return results or [{"message": "No results found"}]

@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 3):
    """
    Search FreeCodeCamp's YouTube channel via RSS by title.
    
    Args:
        query (str): The search term to look for
        max_results (int, optional): Maximum results to return. Defaults to 3.
    
    Returns:
        list: Matching videos or a "no results" message
    """
    feed = feedparser.parse(
        "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    )
    results = []
    query_lower = query.lower()
    
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
            
        if len(results) >= max_results:
            break
    
    return results or [{"message": "No videos found"}]

@mcp.tool()
def fcc_secret_message():
    """Returns an inspirational message."""
    return "Keep exploring! The journey of learning never ends! 🌟"

# Step 4: Run the service with HTTP transport
if __name__ == "__main__":
    print("Starting the FreeCodeCamp Content Explorer with HTTP transport...")
    print("The service will be accessible via HTTP endpoints")
    print("This deployment configuration allows the service to:")
    print("1. Be accessed over HTTP")
    print("2. Handle multiple concurrent requests")
    print("3. Be integrated with web services")
    
    # The key difference is here - we use HTTP transport instead of STDIO
    mcp.run(transport="http")

# Deployment Notes:
# 1. This service uses HTTP transport instead of STDIO
# 2. It can be accessed through HTTP endpoints
# 3. Suitable for production deployment
# 4. Can be containerized and deployed to cloud platforms