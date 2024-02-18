from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

app = FastAPI()

class TravelQuery(BaseModel):
    location: str = Field(..., example="Karachi")
    interests: str = Field(..., example="food, historical sites")

@app.post("/explore/", response_model=TravelQuery)
async def explore(travel_query: TravelQuery):
    try:
        prompt = f"Tell me about must-visit places and recommended local dishes in {travel_query.location} for someone interested in {travel_query.interests}."
        generated_text = generator(prompt, max_length=200)[0]['generated_text']
        return {
            "location": travel_query.location,
            "generated_suggestions": generated_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"Message": "Path Guide GPT API by Ahmed Mujtaba"}
