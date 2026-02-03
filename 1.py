from fastapi import FastAPI,Query,Depends,Form
from fastapi import Header, Cookie
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.get("/items/")
# def read_item(user_agent: str = Header(None), session_token: str = Cookie(None)):
#     return {"User-Agent": user_agent, "Session-Token": session_token}

@app.get("/items/")
def read_item(item: Item, q: str = Query(..., max_length=10)):
    return {"item": item, "q": q}


@app.get("/redirect")
def redirect():
    return RedirectResponse(url="/items/")

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     if item_id == 42:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    content = {"item_id": item_id}
    headers = {"X-Custom-Header": "custom-header-value"}
    return JSONResponse(content=content, headers=headers)



# 依赖项函数
def common_parameters ( q: str = None , skip: int = 0 , limit: int = 100 ) :
    return {"q": q, "skip": skip, "limit": limit}


# 路由操作函数
@app.get("/items1/")
async def read_items( commons: dict = Depends ( common_parameters ) ) :
    return commons


# async def after_request ( ) : 
#     # 这里可以执行一些后处理逻辑，比如记录日志pass # 后处理依赖项@ app. get ( "/items/" , response_model = dict ) async def read_items_after ( request: dict = Depends ( after_request ) ) : return { "message" : "项目成功返回" }


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}