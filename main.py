from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def hommepage():
    return {"message": "Hello Sarita!"}
     