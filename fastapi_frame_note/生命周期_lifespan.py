from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI


def ml_model(x: float):
    return x * 1


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = ml_model  # 程序启动前应执行的逻辑
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()  # 程序关闭时应执行的逻辑


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
