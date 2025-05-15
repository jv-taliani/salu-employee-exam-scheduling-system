from datetime import datetime, date
from uuid import UUID
from clinic import Clinic, OpeningHours
from employee import Employee
from exam_scheduler import ExamSchedulerClass
from exam_type_enum import ExamTypeEnum
from memory import clinics, employees, exams

clinics.clear()
employees.clear()
exams.clear()

clinic = Clinic(
    id=UUID("87654321-4321-8765-4321-567843210987"),
    name="Clinic one",
    exam_types=[ExamTypeEnum.GENERAL_CHECKUP],
    opening_hours=OpeningHours(),
)

employee = Employee(
    id=UUID("12345678-1234-5678-1234-567812345678"),
    name="Joaquim",
    birth=date(1990, 2, 14),
    company="Google",
)

clinics.append(clinic)
employees.append(employee)

sheduler = ExamSchedulerClass()

result = sheduler.execute(  # agendamento dentro do horario da clínica
    employee_id=employee.id,
    clinic_id=clinic.id,
    exam_type=ExamTypeEnum.GENERAL_CHECKUP,
    exam_start=datetime(2023, 10, 16, 14, 0),
)
print(result)

result = sheduler.execute(  # agendamento fora do horario da clínica
    employee_id=employee.id,
    clinic_id=clinic.id,
    exam_type=ExamTypeEnum.GENERAL_CHECKUP,
    exam_start=datetime(2023, 10, 16, 6, 0),
)
print(result)

result = sheduler.execute(  # agendamento com conflito de horário
    employee_id=employee.id,
    clinic_id=clinic.id,
    exam_type=ExamTypeEnum.GENERAL_CHECKUP,
    exam_start=datetime(2023, 10, 16, 14, 30),
)
print(result)
