from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI

# I used Ollama and mistral due to not having openai access
model = Ollama(
    model="mistral:7b-instruct-q4_0"
) 

# use this for Open AI connection.
# os.environ["LANGCHAIN_API_KEY"] = 'YOUR_API_KEY'
# model = ChatOpenAI(model="gpt-4")

prompt_template = PromptTemplate.from_template("""You are a bot that generates personalized study plans for students.
Use the following information to make a personalized study plan:                                               
Name: {name}
Field of study: {field}
Year of study: {year}
List of subjects: {subjects}
Preferred Learning Styles: {learning_styles}
Personal Objectives: {objectives}
Challenges: {challenges}
Extracurricular activities: {extracurriculars}
""")

# result = prompt_template.invoke({"topic": "cats"}).text
chain = prompt_template | model

# result = llm.invoke("Tell me a joke")

result = chain.invoke({"name": "ahmed", "field": "Computer Science", "year": "3rd", "subjects": "Math, Physics, Computer Science", "learning_styles": "Visual, Auditory", "objectives": "To get a 4.0 GPA", "challenges": "Procrastination", "extracurriculars": "Football, Chess, Swimming"})

print(result)

## LLM response:
# Hi Ahmed! Based on the information you have provided, here is a personalized study plan that can help you achieve your goal of getting a 4.0 GPA. 

# **Academic Plan:** 
# - **Math:** Spend 2 hours per day practicing problems and reviewing concepts. Use visual aids such as diagrams and graphs to help you understand the material better. 
# - **Physics:** Allocate 3 hours per day for reading and problem-solving. Listen to lectures and use auditory aids like podcasts to enhance your understanding.
# - **Computer Science:** Dedicate 4 hours per day to coding practice and algorithm development. Use visual aids like flowcharts and diagrams to help you structure your code.

# **Study Schedule:** 
# Monday: Math (2 hrs), Football (1 hr)
# Tuesday: Physics (3 hrs), Chess (1 hr)
# Wednesday: Computer Science (4 hrs), Swimming (1 hr)
# Thursday: Math (2 hrs), Physics (3 hrs)
# Friday: Computer Science (4 hrs), Chess (1 hr)
# Saturday: Football (1 hr), Swimming (1 hr)
# Sunday: Rest day or review of the week's material.

# **Time Management Strategies:**
# - Break your study sessions into smaller, manageable chunks. Use a timer to help you stay on track and take regular breaks to avoid burnout.
# - Prioritize your subjects based on their difficulty level and allocate more time to the ones that require more effort.
# - Create a study schedule and stick to it. This will help you maintain a consistent pace and ensure that you cover all the necessary material.

# **Procrastination Management:**
# - Identify the root cause of your procrastination and address it. If you are overwhelmed, break down your tasks into smaller, more manageable ones.
# - Use positive self-talk to motivate yourself and reinforce your study goals. Reward yourself for completing tasks on time.
# - Seek help from a mentor or tutor if needed. They can provide guidance and support to help you stay on track.

# **Extracurricular Activities:**
# - Use your extracurricular activities as a way to relax and recharge. They can also help you develop important skills like teamwork, leadership, and time management.

# I hope this study plan helps you achieve your academic goals. Remember to stay consistent, focused, and motivated, and don't hesitate to seek help if needed. Good luck!