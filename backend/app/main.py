from datetime import date
from pathlib import Path
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, String, Integer, Date, Boolean, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

BASE = Path(__file__).resolve().parent.parent
STATIC = BASE / "static"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE / 'triade.db'}")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

class Base(DeclarativeBase): pass

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(160), index=True)
    registration: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    class_id: Mapped[int | None] = mapped_column(ForeignKey("school_classes.id"), nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

class SchoolClass(Base):
    __tablename__ = "school_classes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

class Attendance(Base):
    __tablename__ = "attendance"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), index=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("school_classes.id"), index=True)
    day: Mapped[date] = mapped_column(Date, index=True)
    present: Mapped[bool] = mapped_column(Boolean)

Base.metadata.create_all(engine)
app = FastAPI(title="Tríade Digital API", version="0.1.0",
              description="MVP acadêmico — dados fictícios.")
app.mount("/static", StaticFiles(directory=STATIC), name="static")

class StudentIn(BaseModel):
    name: str = Field(min_length=2, max_length=160)
    registration: str = Field(min_length=1, max_length=40)
    class_id: int | None = None
class ClassIn(BaseModel):
    name: str = Field(min_length=2, max_length=100)
class AttendanceIn(BaseModel):
    student_id: int
    class_id: int
    day: date
    present: bool

@app.get("/")
def home(): return FileResponse(STATIC / "index.html")

@app.get("/api/health")
def health(): return {"status":"ok","project":"Tríade Digital","version":"0.1.0"}

@app.get("/api/classes")
def list_classes():
    with Session(engine) as s:
        return [{"id":c.id,"name":c.name} for c in s.scalars(select(SchoolClass).order_by(SchoolClass.name))]

@app.post("/api/classes", status_code=201)
def create_class(data: ClassIn):
    with Session(engine) as s:
        if s.scalar(select(SchoolClass).where(SchoolClass.name == data.name)):
            raise HTTPException(409, "Turma já cadastrada")
        c=SchoolClass(name=data.name); s.add(c); s.commit(); s.refresh(c)
        return {"id":c.id,"name":c.name}

@app.get("/api/students")
def list_students():
    with Session(engine) as s:
        rows=s.scalars(select(Student).where(Student.active == True).order_by(Student.name)).all()
        classes={c.id:c.name for c in s.scalars(select(SchoolClass)).all()}
        return [{"id":x.id,"name":x.name,"registration":x.registration,
                 "class_id":x.class_id,"class_name":classes.get(x.class_id,"—")} for x in rows]

@app.post("/api/students", status_code=201)
def create_student(data: StudentIn):
    with Session(engine) as s:
        if s.scalar(select(Student).where(Student.registration == data.registration)):
            raise HTTPException(409, "Matrícula já cadastrada")
        if data.class_id and not s.get(SchoolClass, data.class_id):
            raise HTTPException(404, "Turma não encontrada")
        x=Student(name=data.name,registration=data.registration,class_id=data.class_id)
        s.add(x); s.commit(); s.refresh(x)
        return {"id":x.id,"name":x.name,"registration":x.registration,"class_id":x.class_id}

@app.put("/api/students/{student_id}")
def update_student(student_id: int, data: StudentIn):
    with Session(engine) as s:
        x=s.get(Student,student_id)
        if not x: raise HTTPException(404,"Estudante não encontrado")
        duplicate=s.scalar(select(Student).where(Student.registration==data.registration,Student.id!=student_id))
        if duplicate: raise HTTPException(409,"Matrícula já cadastrada")
        x.name=data.name; x.registration=data.registration; x.class_id=data.class_id
        s.commit(); return {"message":"Estudante atualizado"}

@app.delete("/api/students/{student_id}")
def delete_student(student_id: int):
    with Session(engine) as s:
        x=s.get(Student,student_id)
        if not x: raise HTTPException(404,"Estudante não encontrado")
        x.active=False; s.commit()
        return {"message":"Estudante inativado"}

@app.post("/api/attendance", status_code=201)
def record_attendance(data: AttendanceIn):
    with Session(engine) as s:
        if not s.get(Student,data.student_id): raise HTTPException(404,"Estudante não encontrado")
        if not s.get(SchoolClass,data.class_id): raise HTTPException(404,"Turma não encontrada")
        existing=s.scalar(select(Attendance).where(Attendance.student_id==data.student_id,
            Attendance.day==data.day))
        if existing:
            existing.present=data.present; existing.class_id=data.class_id
            s.commit(); return {"message":"Frequência atualizada"}
        s.add(Attendance(student_id=data.student_id,class_id=data.class_id,day=data.day,present=data.present))
        s.commit(); return {"message":"Frequência registrada"}

@app.get("/api/alerts")
def alerts():
    with Session(engine) as s:
        students=s.scalars(select(Student).where(Student.active==True)).all()
        result=[]
        for st in students:
            records=s.scalars(select(Attendance).where(Attendance.student_id==st.id)
                              .order_by(Attendance.day.desc())).all()
            streak=0; last_day=None
            for r in records:
                if r.present: break
                streak += 1
                if last_day is None: last_day=r.day
            if streak >= 3:
                result.append({"student_id":st.id,"student":st.name,"registration":st.registration,
                               "consecutive_absences":streak,"last_absence":str(last_day),
                               "class_id":st.class_id})
        return result
