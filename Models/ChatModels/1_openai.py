from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  

model = ChatOpenAI(model="gpt-3.5-turbo") 
# model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10) set temp for the variety of responses 
# for temp refer image.png
 
result = model.invoke("What is the capital of India?")

print(vars(result)) 

#only for content 
print(result.content)

