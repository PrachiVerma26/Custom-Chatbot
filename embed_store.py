from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define your OpenAI API Key
openai_api_key = "Add your own API Key"

# Create an embedding model
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Sample documents (Replace with your dataset)
texts = ["Hello, how can I help you?", "This is a chatbot using FAISS and Langchain."]

# Create FAISS index
vectorstore = FAISS.from_texts(texts, embeddings)

# Save FAISS index
vectorstore.save_local("faiss_index")

print("FAISS index created and saved successfully.")
