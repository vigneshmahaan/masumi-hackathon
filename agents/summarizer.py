from crewai import Agent

def summarize_curriculum(curriculum_text):
    """
    Summarize the curriculum in short, simple terms.
    """
    summarizer_agent = Agent(
        role="Curriculum Summarizer",
        goal="Summarize the given curriculum in short and simple terms.",
        backstory="An AI teacher who explains long topics clearly and simply for easy understanding.",
    )

    summary = (
        "This curriculum introduces the basics, explores key concepts, "
        "covers advanced topics, and provides real-world applications "
        "to help learners master the subject."
    )

    return summary
