from langchain_community.llms import ollama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.schema.output_parser import StrOutputParser
from langchain.schema import AIMessage, HumanMessage,SystemMessage

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    HumanMessage(content="You are a sales person in a store named Electronics World {name}, state the approximate price of the product and negotiate the price with the buyers offer them max of 20 percentage from the initial price,convince them and seal the deal"),
    MessagesPlaceholder("chat_history")
]
prompt_template = ChatPromptTemplate.from_messages(messages)
chat_history = []
name = input("Enter Your Name: ")

# Remove the SystemMessage and use a HumanMessage instead
chat_history.append(HumanMessage(content=f"You are a sales person in a store named Electronics World {name}, negotiate the price with the buyers offer them max of 20 percentage from the initial price,convince them and seal the deal"))

while True:
    query = input(f"{name}: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))
    chain = prompt_template | model | StrOutputParser()
    result = chain.invoke({"name": name, "chat_history": chat_history})
    response = result
    chat_history.append(AIMessage(content=response))

    print(f"AI {response}")