import os
import gradio as gr
from agents.curriculum_builder import generate_curriculum
from agents.summarizer import summarize_curriculum
from agents.quiz_creator import create_quiz

def run_agent(topic):
    curriculum = generate_curriculum(topic)
    summary = summarize_curriculum(curriculum, topic)
    quiz = create_quiz(curriculum, topic)
    return curriculum, summary, quiz

iface = gr.Interface(
    fn=run_agent,
    inputs=gr.Textbox(lines=1, placeholder="Enter a topic"),
    outputs=[
        gr.Textbox(label="Curriculum"),
        gr.Textbox(label="Summary"),
        gr.Textbox(label="Quiz")
    ],
    title="Curriculum AI Agent",
    description="Generates curriculum, summary, and quiz for any topic."
)

# ✅ Corrected launch for Railway
if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))  # Railway gives dynamic port
    iface.launch(server_name="0.0.0.0", server_port=port, share=True)
