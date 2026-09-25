"""
FABLE - SIH26152 backend entrypoint.
Owner: Ashwin (Data/Backend + Integration)

Run with:
    uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs to test endpoints in the browser.
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FABLE - SIH26152 Analytics API")

# Allow the frontend (served separately, e.g. from a different port) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this before deployment
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Basic health check. Visit http://127.0.0.1:8000/ to confirm the server is running."""
    return {"status": "ok", "message": "FABLE backend is running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Step 1 stub: accept a file and confirm it was received.
    Ashwin: replace the body of this function with real parsing
    (see backend/modules/data_processing.py) once this endpoint
    is confirmed working end-to-end.
    """
    contents = await file.read()
    return {
        "filename": file.filename,
        "size_bytes": len(contents),
        "message": "File received. Analysis not implemented yet.",
    }
