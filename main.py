from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate #allows for easy interaction with LLMs

#template for how it should respond to queries

template = """"
Answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer: 
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)
#chain the model and prompt together using langchain
chain = prompt | model

result = chain.invoke({"context": "", "question": "How good are you?"})
print(result)
