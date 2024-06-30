from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from backend.main_agent import MainAgent  # Absolute import

app = FastAPI()
main_agent = MainAgent()

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    file_location = f"./uploaded_files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    document_content = "Extracted content from the document"  # Replace with actual content extraction logic
    return JSONResponse(content={"filename": file.filename, "document_id": file.filename, "document_content": document_content})

@app.post("/ask/")
async def ask_question(question: str, document_id: str):
    document_content = "This is the document content"  # Replace with actual content retrieval logic

    results = main_agent.assign_tasks(document_content, question)
    return JSONResponse(content=results)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
