from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42) 

app = FastAPI()

class TravelQuery(BaseModel):
    location: str
    interests: str

@app.post("/explore/")
async def explore(travel_query: TravelQuery):
    prompt = f"Give me a list of must-visit places and recommended local dishes to try in {travel_query.location}. I am interested in {travel_query.interests}."
    
    response = generator(prompt, max_length=200, num_return_sequences=1)
    
    generated_text = response[0]['generated_text']
    
    return {
        "location": travel_query.location,
        "generated_suggestions": generated_text
    }
