from flask import Flask, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

app = Flask(__name__)

# Step 4: Load stored embeddings
openai_api_key = "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"
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)


# Step 5: Set up a retrieval-based chatbot
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(openai_api_key=openai_api_key),
    retriever=vectorstore.as_retriever()
)

@app.route('/ask', methods=['POST'])
def ask():
    """Handles user queries and returns responses."""
    query = request.json.get("question")
    if not query:
        return jsonify({"error": "Please provide a question"}), 400

    response = qa_chain.run(query)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)
