def create_quiz(curriculum_text: str, topic: str) -> str:
    """Generate 5 simple quiz questions."""
    quiz = [
        f"1. What is the main goal of studying {topic}?",
        f"2. List the core concepts of {topic}.",
        f"3. Name one practical application of {topic}.",
        f"4. Suggest a real-world project related to {topic}.",
        f"5. How can you apply {topic} knowledge in daily life?"
    ]
    return "\n".join(quiz)
