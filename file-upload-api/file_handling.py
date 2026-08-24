from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles

import os
import re
import shutil

UPLOAD_FOLDER = "uploads"

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=UPLOAD_FOLDER),
    name="static"
)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    # 1. SAFE FILENAME HANDLING

    filename = file.filename or ""

    filename = filename.replace("\\", "/")

    safe_filename = os.path.basename(filename)

    safe_filename = re.sub(
        r"[^a-zA-Z0-9._-]",
        "_",
        safe_filename
    )

    safe_filename = safe_filename.lower()

    # Make sure the filename is not empty
    if not safe_filename or safe_filename in {".", ".."}:
        raise HTTPException(
            status_code=400,
            detail="Invalid filename."
        )


    # 2. FILE TYPE VALIDATION

    extension = os.path.splitext(safe_filename)[1]

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=415,
            detail=(
                "Unsupported file type. "
                "Allowed types: JPG, JPEG, PNG, PDF, TXT."
            )
        )

    # 3. FILE SIZE VALIDATION

    file.file.seek(0, 2)

    file_size = file.file.tell()

    file.file.seek(0)

    if file_size == 0:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty."
        )

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size must not exceed 5 MB."
        )


    # 4. CREATE FILE PATH

    file_path = os.path.join(
        UPLOAD_FOLDER,
        safe_filename
    )


    # 5. DUPLICATE FILE CHECK

    if os.path.exists(file_path):
        raise HTTPException(
            status_code=409,
            detail="A file with this name already exists."
        )


    # 6. SAVE FILE

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )


    # 7. CREATE FILE URL

    file_url = f"/static/{safe_filename}"


    # 8. RESPONSE

    return {
        "message": "File uploaded successfully.",
        "filename": safe_filename,
        "file_size": file_size,
        "file_type": extension,
        "file_url": file_url
    }
