from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# السماح للفرونت إند بالتفاعل مع الباك إند
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل بيانات الإكسل
FILE_PATH = "/mnt/data/data.xlsm"
df = pd.read_excel(FILE_PATH, engine="openpyxl")

@app.get("/search/")
def search_student(student_id: int):
    result = df[df['ID'] == student_id]
    if result.empty:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student_data = result.iloc[0][['ID', 'Name', 'Doctor', 'Mobile']].to_dict()
    return student_data

# تقديم ملفات الواجهة الأمامية
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")
