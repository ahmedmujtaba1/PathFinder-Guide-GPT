from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline('text-generation', model='gpt2')

class ExplorationQuery(BaseModel):
    prompt: str
    max_length: int = 50

@app.post("/explore/")
async def explore(query: ExplorationQuery):
    """
    Generate exploration guidance based on a prompt.
    The prompt could be something like "What are the best places to visit in Paris for art lovers?"
    """
    generated_texts = generator(query.prompt, max_length=query.max_length, return_full_text=False)
    return {"guidance": generated_texts[0]['generated_text']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
