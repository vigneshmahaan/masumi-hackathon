from agents.curriculum_builder import generate_curriculum
from agents.summarizer import summarize_curriculum
from agents.quiz_creator import create_quiz

def main():
    print("\n=== 🎓 Curriculum AI Agent Started ===\n")

    topic = input("Enter the topic you want a curriculum for: ").strip()
    if not topic:
        print("❗ No topic provided. Exiting.")
        return

    curriculum = generate_curriculum(topic)
    print("\n🧾 Generated Curriculum:\n", curriculum)

    summary = summarize_curriculum(curriculum, topic)
    print("\n📝 Summary:\n", summary)

    quiz = create_quiz(curriculum, topic)
    print("\n❓ Quiz Questions:\n", quiz)

    print("\n✅ Done!")

if __name__ == "__main__":
    main()
