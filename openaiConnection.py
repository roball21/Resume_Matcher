import openai
import os
from dotenv import load_dotenv
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



class EmbeddingAndComparison:
    def __init__(self,  resume_file, jobs_file, model="text-embedding-3-small"):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
        self.resume_file = resume_file
        self.jobs_file = jobs_file

        self.resume_embedding = None
        self.job_embeddings = []
        self.results = []

    def embed_text(self, text):
        response = openai.embeddings.create(
            input=text, 
            model=self.model
        )
        return [item.embedding for item in response.data]
        
    
    def embed_and_cache(self, text_list, cache_path):
        if os.path.exists(cache_path):
            print(f"Using cached embedding from {cache_path}")
            return np.load(cache_path)
        print(f"[INFO] Embedding {len(text_list)} texts and caching to '{cache_path}'")
        embeddings = self.embed_text(text_list)
        np.save(cache_path, np.array(embeddings))
        return np.array(embeddings)
    
    def compare(self, single_embedding, multiple_embeddings):
        similarities = cosine_similarity([single_embedding], multiple_embeddings)[0]
        return similarities
    
    def run(self, resume_cache="resume_embedding.npy", job_cache="job_embeddings.npy"):
        with open(self.resume_file) as f:
            resume_data = json.load(f)
        with open(self.jobs_file) as f:
            job_data = json.load(f)

        resume_text = resume_data["resume"]
        job_texts = [
            ", ".join(job.get("job_highlights", {}).get("Qualifications", []))
            for job in job_data
        ]


        resume_embedding = self.embed_and_cache([resume_text], resume_cache)[0]
        job_embeddings = self.embed_and_cache(job_texts, job_cache)

        scores = self.compare(resume_embedding, job_embeddings)

        # sorting based on similarity score
        ranked = sorted(zip(job_data, scores), key=lambda x: x[1], reverse=True) 

        print("\n Top job matches:\n")
        for job, score in ranked:
            print(f"- {job['title']}: {score:.4f}")

        return ranked
