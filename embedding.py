from sentence_transformers import SentenceTransformer
import faiss
import pickle as pkl
from scrap import chunks


docs = []
with open('angel_data.pkl','rb') as f:
    data = pkl.load(f)
    print(data)
    for items in data:
        docs.append(chunks(items))


model = SentenceTransformer('all-MiniLM-L6-v2')
docs_embeddings = model.encode(docs)

index = faiss.IndexFlatL2(docs_embeddings.shape[1])
index.add(docs_embeddings)
faiss.write_index(index,'faiss_index.idx')
pkl.dump(docs,open('docs.pkl','wb'))