from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from utils import parseDocument, parseLink

app = FastAPI()
origins = [
"http://localhost:3000", # Your React app's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
async def get_data():
    return {"message": "Data from Python backend!"}

@app.post("/parse", response_class=PlainTextResponse)
async def parse_endpoint(input_type: str = Form(...), 
                    link: str = Form(None), 
                    file: UploadFile = File(None)):

    if input_type == "link" and link:
        content = parseLink.fetch_url_text(link)
        return content
    elif input_type == "file" and file:
        content = await parseDocument.parse_file(file)
        return content
    else:
        return {"error": "Invalid input."}