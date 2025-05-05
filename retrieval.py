import faiss 
import pickle as pkl
from sentence_transformers import SentenceTransformer
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from transformers import pipeline

pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B")

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index('faiss_index.idx')
docs = pkl.load(open('docs.pkl','rb'))

def retrieve(query,top_k=3):
    query_embedding = model.encode([query])
    dist, idx = index.search(query_embedding,top_k)
    # print(dist)
    if dist[0][0] > 2.0:
        return []
    
    return [docs[i] for i in idx[0]]

def generate_answer(query):
    context = retrieve(query)
    if not context:
        return "I don't Know"
    # print(context)
    
    prompt = f"Answer the question using only the following information:\n{''.join(context[0])}\n\nQuestion: {query}"

    result = pipe(prompt, max_new_tokens=100)[0]['generated_text']

    return result

q = 'Why do I need to verify my mobile number?'
print(generate_answer(q))