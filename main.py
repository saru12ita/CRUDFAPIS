from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_tasks
from database.models import Todo


app=FastAPI()
router=APIRouter()

@router.get("/")
async def get_all_todos():
    data=collection.find()
    return all_tasks(data)

@router.post("/")
async def create_task(new_task: Todo):
    try:
       resp= collection.insert_one(dict(new_task))
    except Exception as e:
        return HTTPException(status_code=500, detail=f"some error occure {e}")

app.include_router(router)