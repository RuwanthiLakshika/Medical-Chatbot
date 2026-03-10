# Medibot Chatbot - Medical AI Assistant

Medibot is an end-to-end medical chatbot powered by Generative AI and Retrieval Augmented Generation (RAG). It provides accurate, context-aware medical information by leveraging a knowledge base without hallucinating responses.

### Features
- RAG-Powered Responses: Retrieves relevant medical context before generating answers, ensuring accuracy and reliability
- Medical-Focused Assistant: Specialized system prompt that answers only using provided medical context
- Web-Based Interface: Clean, user-friendly chat interface built with Flask
- Semantic Search: Uses vector embeddings and Pinecone to find the most relevant medical information
- Safe Responses: Never makes up answers - explicitly states when information is unavailable
- Real-time Conversations: Interactive chat experience with instant responses
  
### Tech Stack
- Backend: Flask (Python)
- LLM: Cohere's Command R+ Model
- Vector Store: Pinecone
- Embeddings: HuggingFace Embeddings
- Frontend: HTML/CSS with JavaScript

### How It Works
1. User submits a medical query through the chat interface
2. The query is converted to embeddings using HuggingFace
3. Pinecone retrieves the 3 most relevant documents from the medical knowledge base
4. Cohere's language model generates a response based only on the retrieved context
5. The response is displayed to the user in real-time

<img width="962" height="662" alt="image" src="https://github.com/user-attachments/assets/340133b6-38f2-471a-96bd-00e23fd0dcc7" />

<img width="1872" height="861" alt="image" src="https://github.com/user-attachments/assets/2d524de0-81e5-43d0-a2ba-624f594ee7bf" />

### How to run?
#### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
#### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


#### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


#### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
COHERE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


#### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone


