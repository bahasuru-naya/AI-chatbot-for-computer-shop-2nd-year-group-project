# app.py
from flask import Flask, render_template, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders.mongodb import MongodbLoader
from dotenv import load_dotenv
import os




app = Flask(__name__)

# Load environment variables
load_dotenv()



# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Initialize MongoDB loader
loader = MongodbLoader(
    connection_string = "mongodb+srv://gpsd:helloworld@gpsd0.3fvcw.mongodb.net/?retryWrites=true&w=majority&appName=gpsd0",
    db_name="ComputerStore",
    collection_name="merged_collection",
    field_names=[
    "_id",
    "id",
    "item_name",
    "Item_Pic_Url",
    "Item_detail",
    "stock",
    "price",
    "warranty_in_months",
    "sales",
    "SaleID",
    "QuantitySold",
    "SaleDate"
])
# Load documents and create vector store
all_docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=20)
splits = text_splitter.split_documents(all_docs)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()

document_cont = ""
for i in range(len(all_docs)):
    document_cont += all_docs[i].page_content + "\n" 

system_prompt = """
You are a helpful chatbot designed to assist a shop owner in managing their business. Your primary functions include:
- greet when user give "Hi","Hello"
- Do not provide Full Decriptive answers if user didn't ask for detailed answers
- Offering inventory management tips.
- Assisting with sales strategies and customer relationship management.
- Helping with billing and bookkeeping queries.
- Sharing marketing and promotional ideas tailored to small businesses.
- Guiding the user with logistics and supplier management.
- Answering any general inquiries related to running a shop effectively.

# Key Features:
- MUST Greet if user send you like "Hi","Hello","Hey"
- Maintain a professional and friendly tone in all interactions.
- Use clear and concise language to ensure your advice is actionable.
- Anticipate common business-related questions and provide suggestions proactively.
- Personalize responses to make them as relevant as possible.

# Output format:
- Ensure all outputs are in a clear and readable message format.
- Avoid technical jargon unless specifically requested by the user.
- Provide step-by-step instructions where applicable.'
- You can use emojis as well


{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# Create chains
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query', '')
    if not user_query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        response = rag_chain.invoke({"input": user_query+"Here's the mongodb data"+document_cont})
        formatted_response = format_response(response['answer'])
        return jsonify({'response': formatted_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def format_response(response_text):
    import re
    formatted_text = re.sub(r"\*\*", "", response_text)
    formatted_text = formatted_text.replace("\\n", "\n")
    return formatted_text

if __name__ == '__main__':
    app.run(debug=True)