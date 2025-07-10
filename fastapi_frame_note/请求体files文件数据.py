import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...) ):
    print(files)
    for file in files:
        print(file.filename)

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        file_path = os.path.join(file_path, "_" + file.filename)
        print(file_path)

        content = await file.read() 
        with open(file_path, "wb") as f:
            f.write(content)

        content = content.decode('utf-8')
        print(content)

    return HTMLResponse(content="<p>ok!</p>")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
