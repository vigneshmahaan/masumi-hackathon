import wikipedia
from ddgs import DDGS

def fetch_topic_content(topic: str) -> str:
    """Fetch Wikipedia summary for a topic (first 3 paragraphs)."""
    try:
        wiki = wikipedia.page(topic)
        paragraphs = wiki.content.split("\n\n")
        return "\n\n".join(paragraphs[:3])
    except Exception:
        return None

def search_duckduckgo(query: str, max_results: int = 5):
    """Fetch DuckDuckGo snippets."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        processed = []
        for r in results:
            processed.append({
                "title": r.get("title", ""),
                "href": r.get("link", ""),  # corrected key
                "snippet": r.get("body", "")
            })
        return processed
