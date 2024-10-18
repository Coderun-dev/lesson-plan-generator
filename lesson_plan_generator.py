teacher_input = {
    "grade": "5th Grade",
    "subject": "Science",
    "learning_objectives": "Understand the water cycle",
    "teaching_style": "Inquiry-based learning",
    "assessment_content": "Quiz on water cycle, Group Project",
    "materials": "Water cycle model, Diagrams"
}

prompt_template = """
You are a lesson plan generation assistant. A teacher has provided the following details for a lesson:

Grade: {grade}
Subject: {subject}
Learning Objectives: {learning_objectives}
Preferred Teaching Style: {teaching_style}
Assessment: {assessment_content}
Materials: {materials}

Please generate a detailed lesson plan including introduction, activities, assessment strategies, and conclusion, following the teacher's preferences.
"""


prompt = prompt_template.format(
    grade=teacher_input["grade"],
    subject=teacher_input["subject"],
    learning_objectives=teacher_input["learning_objectives"],
    teaching_style=teacher_input["teaching_style"],
    assessment_content=teacher_input["assessment_content"],
    materials=teacher_input["materials"]
)
import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "your_openai_api_key"

def generate_lesson_plan(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the model you want to use
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()
