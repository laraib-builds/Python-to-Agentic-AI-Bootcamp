# File Upload API

This is a simple file upload API made using **FastAPI**.

The user can upload a file, and before saving it, the API checks different conditions such as file size, file type, empty files, duplicate files, and filename safety.

If the file passes all validations, it is saved in the `uploads` folder and the API returns a URL to access it.

## Features

* Upload files using FastAPI
* Maximum file size limit of **5 MB**
* Only allows:

  * `.jpg`
  * `.jpeg`
  * `.png`

* Rejects empty files
* Prevents duplicate filenames
* Handles unsafe filenames
* Converts filenames to lowercase
* Replaces unsafe characters with `_`
* Handles both `/` and `\` in filenames
* Provides a URL to access uploaded files

## Validations and Exceptions

The API uses `HTTPException` for invalid requests.

| Validation             | Status Code |
| ---------------------- | ----------: |
| Invalid/empty filename |         400 |
| Empty file             |         400 |
| File too large         |         413 |
| Unsupported file type  |         415 |
| Duplicate filename     |         409 |

## How It Works

The basic flow is:

```text
Upload file
    ↓
Clean filename
    ↓
Check file type
    ↓
Check file size
    ↓
Check if file already exists
    ↓
Save file
    ↓
Return file URL
```

Uploaded files are stored inside the `uploads` folder.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* `os`
* `re`
* `shutil`

## Running the Project

Install the required packages and run the FastAPI application with Uvicorn.

For example:

```bash
uvicorn main:app --reload
```

Then open the Swagger UI:

```text
http://127.0.0.1:8000/docs
```

From there, the `/upload` endpoint can be tested by uploading a file.

## What I Learned

While working on this project, I learned how to:

* Handle file uploads with `UploadFile`
* Use `HTTPException` for API errors
* Validate user input
* Check file size
* Check file extensions
* Work with file paths using `os`
* Safely handle filenames
* Save and copy files using Python
* Serve uploaded files using `StaticFiles`
* Understand how an API processes a request before returning a response
