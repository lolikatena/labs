from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia as wiki
import random

app = FastAPI()
wiki.set_lang("ru")

class TitleOut(BaseModel):
    title: str

class SearchOut(BaseModel):
    query: str
    text: str

class NoteIn(BaseModel):
    user: str
    title: str

class NoteOut(BaseModel):
    user: str
    text: str


@app.get("/", summary="Приветствие")
async def read_root():
    return {"message": "Добро пожаловать!"}


@app.get("/path/{page_title}", response_model=TitleOut, summary="Заголовок страницы")
async def get_title(page_title: str):
    page = wiki.page(page_title, auto_suggest=False, redirect=True)
    return TitleOut(title=page.title)


@app.get("/query/", response_model=SearchOut, summary="Поиск")
async def get_info(query: str):
    search_results = wiki.search(query)
    random_result = random.choice(search_results)
    summary = wiki.summary(random_result, sentences=3, auto_suggest=False, redirect=True)
    return SearchOut(query=random_result, text=summary)


@app.post("/", response_model=NoteOut, summary="Создать заметку")
async def post_note(note_input: NoteIn):
    search_results = wiki.search(note_input.title)
    random_result = random.choice(search_results)
    summary = wiki.summary(random_result, sentences=3, auto_suggest=False, redirect=True)
    return NoteOut(user=note_input.user, text=summary)