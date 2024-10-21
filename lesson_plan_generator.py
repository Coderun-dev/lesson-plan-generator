import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "[ENTER OPENAI API KEY HERE]"
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
    duration = st.text_input('Duration', "60 minutes")
    class_size = st.text_input('Class Size', "25 students")
    subject = st.text_input('Subject', "Counseling and Guidance")
    topic = st.text_input('Topic', "Empathy")
    learning_objectives = st.text_area('Learning Objectives', "Identify ways to show empathy")
    teaching_style = st.text_input('Teaching Style', "Knowledge Building")
    assessment_content = st.text_area('Assessment Content', "Worksheet, Group Presentation")
    materials = st.text_area('Materials', "Youtube videos, Diagrams, Padlet discussion")

    if st.button('Generate Lesson Plan'):
        # Create prompt dynamically
        teacher_input = {
            "grade": grade,
            "duration": duration,
            "class_size": class_size,
            "subject": subject,
            "topic": topic,
            "learning_objectives": learning_objectives,
            "teaching_style": teaching_style,
            "assessment_content": assessment_content,
            "materials": materials
        }

        prompt_template = """
        You are a lesson plan generation assistant. A teacher has provided the following details for a lesson:

        Grade: {grade}
        Duration: {duration}
        Class Size: {class_size}
        Subject: {subject}
        Topic: {topic}
        Learning Objectives: {learning_objectives}
        Preferred Teaching Style: {teaching_style}
        Assessment: {assessment_content}
        Materials: {materials}

        Please generate a detailed lesson plan including introduction, activities, assessment strategies, and conclusion, following the teacher's preferences.
        """

        prompt = prompt_template.format(
            grade=teacher_input["grade"],
            duration=teacher_input["duration"],
            class_size=teacher_input["class_size"],
            subject=teacher_input["subject"],
            topic=teacher_input["topic"],
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
