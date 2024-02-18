from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

app = FastAPI()

class TravelQuery(BaseModel):
    location: str
    interests: str

@app.post("/explore/")
async def explore(travel_query: TravelQuery):
    prompt = f"Give me a list of must-visit places and recommended local dishes to try in {travel_query.location}. I am interested in {travel_query.interests}."
    
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    en_text = model.generate(input_ids, max_length=200)
    
    return {
        "location": travel_query.location,
        "generated_suggestions": en_text
    }
