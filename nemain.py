from fastapi import FastAPI 
from pydantic import BaseModel 
import pyjokes 

app = FastAPI() 

class Joke(BaseModel): 
    friend: str 
    joke: str 

class JokeInput(BaseModel): 
    friend: str 


@app.post("/", response_model= Joke) 
def create_joke(joke_input: JokeInput): 
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke(language="ru"))