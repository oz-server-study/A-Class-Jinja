from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models import TodoItem

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")
templates.env.globals['enumerate'] = enumerate  # Jinja2 환경에 enumerate 함수 추가

# 메모리에 데이터를 저장하는 방식 (간단한 예시)
todos = []


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})


@app.post("/add", response_class=RedirectResponse)
async def add_todo(request: Request, title: str = Form(...)):
    todos.append(TodoItem(title=title))
    return RedirectResponse(url="/", status_code=303)


@app.post("/toggle/{index}", response_class=RedirectResponse)
async def toggle_todo(request: Request, index: int):
    if index >= len(todos):
        raise HTTPException(status_code=404, detail="Item not found")
    todos[index].completed = not todos[index].completed
    return RedirectResponse(url="/", status_code=303)


@app.post("/delete/{index}", response_class=RedirectResponse)
async def delete_todo(request: Request, index: int):
    if index >= len(todos):
        raise HTTPException(status_code=404, detail="Item not found")
    todos.pop(index)
    return RedirectResponse(url="/", status_code=303)
