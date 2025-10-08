from crewai import Agent

def create_quiz(curriculum_text):
    """
    Generate 5 simple quiz questions from the given curriculum.
    """
    quiz_agent = Agent(
        role="Quiz Generator",
        goal="Generate 5 simple quiz questions from the given curriculum.",
        backstory="An AI quiz master who tests understanding using short, clear questions.",
    )

    quiz = [
        "1. What are the key concepts discussed in the curriculum?",
        "2. What are the practical applications of this topic?",
        "3. What is the main goal of studying this subject?",
        "4. List one real-world project related to this topic.",
        "5. How can you apply this knowledge in everyday life?"
    ]

    return "\n".join(quiz)
