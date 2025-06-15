from fastapi import FastAPI, Request
import uuid
import os

app = FastAPI()

SAVE_DIR = "saved_files"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.post("/save")
async def save_to_file(request: Request):
    data = await request.json()
    text = ""
    for key, value in data.items():
        text += f"{key}: {value}\n"

    file_name = f"{uuid.uuid4()}.txt"
    file_path = os.path.join(SAVE_DIR, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    return {"message": "File salvato", "filename": file_name}
