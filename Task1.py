from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

# I used Ollama and mistral due to not having openai access
model = Ollama(
    model="mistral:7b-instruct-q4_0"
)

# use this for Open AI connection.
# os.environ["LANGCHAIN_API_KEY"] = 'YOUR_API_KEY'
# model = ChatOpenAI(model="gpt-4")

prompt_template = PromptTemplate.from_template("""You are a bot that generates a social media post.
context:
Q1: Can you describe the specific case study or transformation story you want to share?
Ans1: successful collaboration between Sodexo and CoachHub to accelerate leadership
development across the APMEA region.
Q2: What challenge or problem was addressed in this case?
Ans2: The challenge addressed in this case was the need for scalable leadership
development programs that could effectively engage and develop employees across diverse
geographic regions, particularly in the Asia Pacific, Middle East, and Africa (APMEA).
Q3: What were the key results or outcomes achieved in this story?
Ans3: The key results achieved in this story include the implementation of scalable coaching
programs powered by AI and analytics, which led to improved knowledge retention,
enhanced leadership skills, and increased employee engagement across the APMEA region.
Q4: Are there any data, quotes, or testimonials that illustrate the impact?
Ans4: 75%\ of classroom-style training is forgotten if it's not implemented within 6 days after.
Q5: Is there a specific call-to-action?
Ans5: Join thousands of coachees like Sodexo's Head of FMCG Accounts, Jean Baptiste
CALEMARD, on a journey of growth and transformation to explore the greater you.
Q6: Are there any specific hashtags you'd like to include?
Ans6:
#ExploreTheGreaterYou

Q7: Describe your desired tone and style.
Ans7: professional and make sure to write the achievements in the form of points.

Social media Post:
Did you know? 75%\ of classroom-style training is forgotten if it's not implemented within 6
days after.
Discover how Sodexo, a world leader in facilities management and food services, joined
forces with CoachHub to accelerate their leadership development across APMEA:
🚀 Scalable coaching programs powered by AI and analytics with local support
🌎 Access to a diverse pool of 3,500 top certified coaches from around the world
🌟 Unlimited, structured coaching sessions and flexibility 24/7 for a hybrid, mobile workforce
🧠 Boost knowledge retention and engagement with global benchmarking
✅ Quick implementation with low administrative burden
Join thousands of coachees like Sodexo's Head of FMCG Accounts, Jean Baptiste
CALEMARD, on a journey of growth and transformation to #ExploreTheGreaterYou                                                                           

Use the following information to generate a social media post:                                               
Q1: Can you describe the specific case study or transformation story you want to share?
Ans1: {Ans1}
Q2: What challenge or problem was addressed in this case?
Ans2: {Ans2}
Q3: What were the key results or outcomes achieved in this story?
Ans3: {Ans3}
Q4: Are there any data, quotes, or testimonials that illustrate the impact?
Ans4: {Ans4}
Q5: Is there a specific call-to-action?
Ans5: {Ans5}
Q6: Are there any specific hashtags you'd like to include?
Ans6: {Ans6}
Q7: Describe your desired tone and style.
Ans7: {Ans7}

Social media Post:
""")

# result = prompt_template.invoke({"topic": "cats"}).text
chain = prompt_template | model

# result = llm.invoke("Tell me a joke")

result = chain.invoke({
    "Ans1": "I want to share a case study about the successful collaboration between Nike and Addidas to improve customer satisfaction.",
    "Ans2": "The challenge addressed in this case was the need to streamline the customer support process and reduce response times.",
    "Ans3": "The key results achieved in this story include a 30%\ reduction in customer wait times, a 20%\ increase in customer satisfaction ratings, and a 15%\ improvement in first-call resolution rates.",
    "Ans4": "One customer testimonial highlights the impact of the improved customer support: 'I used to wait for hours to get a response, but now I receive help within minutes. It has made a huge difference in my experience.'",
    "Ans5": "Take the first step towards improving your customer support by implementing the strategies used by Nike and Addidas. Visit our website to learn more.",
    "Ans6": "#CustomerSupport #CustomerSatisfaction #Improvement",
    "Ans7": "The tone of the post should be informative and highlight the positive outcomes achieved through the collaboration in the form of points."
})

print(result)

# LLM response:
# Did you know that Nike and Adidas joined forces to improve customer satisfaction? 🤝 Here's how they did it:
# ✅ Streamlined the customer support process to reduce response times by 30%
# 🚀 Implemented a global team of 24/7 support agents to handle customer inquiries
# 📈 Increased customer satisfaction ratings by 20%
# 💪 Improved first-call resolution rates by 15%
# Hear from one satisfied customer: 'I used to wait for hours to get a response, but now I receive help within minutes. It has made a huge difference in my experience.'
# Improve your own customer support by implementing the strategies used by Nike and Adidas. Visit our website to learn more. #CustomerSupport #CustomerSatisfaction #Improvement