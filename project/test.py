from datetime import datetime, timedelta, date
from project.clinic import Clinic, OpeningHours
from uuid import UUID
from project.employee import Employee
from project.exam_type_enum import ExamTypeEnum
from project.exam import Exam
from project.memory import exams

clinic = Clinic(
    id=UUID("87654321-4321-8765-4321-567843210987"),
    name="clinic one",
    exam_types=[ExamTypeEnum.GENERAL_CHECKUP],
    opening_hours=OpeningHours(),
)

employee = Employee(
    id=UUID("12345678-1234-5678-1234-567812345678"),
    name="Joaquim",
    birth=date(1990, 2, 14),
    company="Google",
)

exam_start = datetime(2023, 10, 15, 14, 0)

exam = Exam(
    employee_id=UUID("12345678-1234-5678-1234-567812345678"),
    clinic_id=UUID("87654321-4321-8765-4321-567843210987"),
    exam_type=ExamTypeEnum.GENERAL_CHECKUP,
    start_time=exam_start,
    end_time=exam_start + timedelta(hours=1),
)
exams.append(exam)
