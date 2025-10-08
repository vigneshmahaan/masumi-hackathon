import numpy as np
import sounddevice as sd
import pyttsx3
import whisper

from agents.curriculum_builder import generate_curriculum
from agents.summarizer import summarize_curriculum
from agents.quiz_creator import create_quiz

# ------------------- Voice Utilities -------------------

def record_voice(duration: float = 5, fs: int = 16000):
    print("🎤 Speak your topic now …")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()
    print("✅ Recording complete.")
    return audio.flatten()

def transcribe_voice(audio: np.ndarray):
    # Normalize audio for Whisper
    audio = audio / np.max(np.abs(audio))
    audio = audio.astype(np.float32)

    whisper_model = whisper.load_model("base")
    result = whisper_model.transcribe(audio, fp16=False)
    text = result.get("text", "").strip()
    print("📝 Transcribed text:", text)
    return text

def speak_text(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ------------------- Main Agent Workflow -------------------

def main():
    print("\n=== 🎓 Curriculum AI Agent Started ===\n")

    # Step 1: Capture voice input
    audio = record_voice(duration=5)
    topic = transcribe_voice(audio)

    # Fallback if transcription fails
    if not topic:
        topic = input("❗ Could not detect speech. Please type the topic: ")

    # Step 2: Generate Curriculum
    curriculum = generate_curriculum(topic)
    print("\n🧾 Generated Curriculum:\n", curriculum)

    # Step 3: Summarize Curriculum
    summary = summarize_curriculum(curriculum)
    print("\n📝 Summary:\n", summary)

    # Step 4: Generate Quiz
    quiz = create_quiz(curriculum)
    print("\n❓ Quiz Questions:\n", quiz)

    # Step 5: Speak the Curriculum
    print("\n🎧 Reading Curriculum aloud …")
    speak_text(curriculum)

    print("\n✅ All done!")

if __name__ == "__main__":
    main()
