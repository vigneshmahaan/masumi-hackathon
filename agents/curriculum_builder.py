from crewai import Agent

def generate_curriculum(topic):
    """
    Generate a structured 7-day curriculum for the given topic.
    """
    curriculum_agent = Agent(
        role="Curriculum Designer",
        goal=f"Design a structured learning curriculum for {topic}.",
        backstory="An expert in creating well-organized learning materials for students of all levels using AI.",
    )

    sections = [
        f"1. Introduction to {topic}",
        f"2. Core Concepts of {topic}",
        f"3. Advanced Topics in {topic}",
        f"4. Practical Applications of {topic}",
        f"5. Real-World Projects related to {topic}",
        f"6. Summary and Next Steps"
    ]

    curriculum = "\n".join(sections)
    return curriculum
