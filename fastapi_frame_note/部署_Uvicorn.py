from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#  --host TEXT      Bind socket to this host.  [default: 127.0.0.1]
#  --port INTEGER       Bind socket to this port. If 0, an available port will be picked.  [default: 8000]
# Linux: `uvicorn 部署_Uvicorn:app --host 0.0.0.0 --port 80`
