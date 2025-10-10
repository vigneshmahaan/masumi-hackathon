def summarize_curriculum(curriculum_text: str, topic: str) -> str:
    """Generate a short summary."""
    lines = curriculum_text.split("\n")
    summary = " ".join(lines[:5])  # take first few lines as summary
    return f"Summary of {topic}:\n{summary}"
