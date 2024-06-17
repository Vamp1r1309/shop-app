import uvicorn
from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel

from items_views import router as items_router
from users.views import router as users_router


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/calc/")
async def get_calc(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
