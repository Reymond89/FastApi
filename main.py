from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4



app = FastAPI()

students = []

# @app.get("/")
# def mensaje():
#     return "hola mundo"

# @app.get("/login")
# def mensaje():
#     return "ingrese sus datos"

# @app.get("/user/{user_id}")
# def mensaje(user_id: str):
#     return f"el id del usuario es: {user_id}"




class Student(BaseModel):
    id: str
    name: str
    lastname: str
    skills: list[str] = []


# LISTAR ESTUDIANTES

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: str):
    for student in students:
        if student["id"]== id:
            return student
    return "No existe el estudiante"

# GUARDAR ESTUDAINTES
@app.post("/students")
def save_student(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return "Estudiante registrado"

# MODIFICAR O ACTULIZAR ESTUDIANTES
@app.put("/students/{id}")
def update_student(update_student: Student, id:str):
    for student in students:
        if student["id"] == id:
            student["name"]= update_student.name
            student["lastname"]= update_student.lastname
            student["skills"]= update_student.skills
            return "Estudiante modificado"
    return "No existe el estudiante"


# ELIMINAR ESTUDIANTES
@app.delete("/stundents/{id}")
def delete_student(id: str):
    for student in students:
        if student["id"]== id:
            students.remove(student)
            return "Estudiante eliminado"
    return "No existe el estudiante"        