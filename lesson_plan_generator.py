import streamlit as st
import openai

# Access the API key from Streamlit secrets
api_key = st.secrets["api_key"]

# OpenAI API Key
openai.api_key = api_key
# Function to generate lesson plan
def generate_lesson_plan(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
            {"role": "user", "content": prompt}
        ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error generating lesson plan: {str(e)}")
        return None

# Streamlit app
def main():
    st.title("Lesson Plan Generator")

    # Input fields for teacher preferences
    grade = st.text_input('Grade', "8th Grade")
    subject = st.text_input('Subject', "Counseling and Guidance")
    topic = st.text_input('Topic', "Empathy")
    learning_objectives = st.text_area('Learning Objectives', "Identify ways to show empathy")

    if st.button('Generate Lesson Plan'):
        # Create prompt dynamically
        teacher_input = {
            "grade": grade,
            "subject": subject,
            "topic": topic,
            "learning_objectives": learning_objectives,
        }

        prompt_template = """
        You are a lesson plan generation assistant. A teacher has provided the following details for a lesson:

        Grade: {grade}
        Subject: {subject}
        Topic: {topic}
        Learning Objectives: {learning_objectives}

        Please generate a detailed lesson plan including Grade, Subject, Topic, Opening, Introduction, Guided Practice, Independent Practice, Closing, Assessment, Extension Activity, and Homework.
        """

        prompt = prompt_template.format(
            grade=teacher_input["grade"],
            subject=teacher_input["subject"],
            topic=teacher_input["topic"],
            learning_objectives=teacher_input["learning_objectives"],
        )
       # Generate and display the lesson plan
        lesson_plan = generate_lesson_plan(prompt)
        st.write(lesson_plan)

if __name__ == "__main__":
    main()
