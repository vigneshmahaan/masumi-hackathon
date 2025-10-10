from agents.web_fetcher import fetch_topic_content, search_duckduckgo

def generate_curriculum(topic: str) -> str:
    """Generate a simple structured 7-day curriculum based on web content."""
    content = fetch_topic_content(topic)
    if not content:
        search_results = search_duckduckgo(topic, max_results=3)
        content = "\n".join(r['snippet'] for r in search_results if r['snippet'])

    sections = [
        f"1. Introduction to {topic}",
        f"2. Core Concepts of {topic}",
        f"3. Advanced Topics in {topic}",
        f"4. Practical Applications of {topic}",
        f"5. Real-World Projects related to {topic}",
        f"6. Summary and Next Steps"
    ]

    curriculum_text = "\n".join(sections)
    # append fetched content for more detail
    curriculum_text += "\n\n" + content[:1000]  # first 1000 chars
    return curriculum_text
