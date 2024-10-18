import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "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"

# Function to generate lesson plan
def generate_lesson_plan(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# Streamlit app
def main():
    st.title("Lesson Plan Generator")

    # Input fields for teacher preferences
    grade = st.text_input('Grade', "5th Grade")
    subject = st.text_input('Subject', "Science")
    learning_objectives = st.text_area('Learning Objectives', "Understand the water cycle")
    teaching_style = st.text_input('Teaching Style', "Inquiry-based learning")
    assessment_content = st.text_area('Assessment Content', "Quiz on water cycle, Group Project")
    materials = st.text_area('Materials', "Water cycle model, Diagrams")

    if st.button('Generate Lesson Plan'):
        # Create prompt dynamically
        teacher_input = {
            "grade": grade,
            "subject": subject,
            "learning_objectives": learning_objectives,
            "teaching_style": teaching_style,
            "assessment_content": assessment_content,
            "materials": materials
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

        # Generate and display the lesson plan
        lesson_plan = generate_lesson_plan(prompt)
        st.write(lesson_plan)

if __name__ == "__main__":
    main()
