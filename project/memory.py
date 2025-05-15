from typing import List

from uuid import UUID
from project.clinic import Clinic
from project.employee import Employee
from project.exam import Exam

clinics: List[Clinic] = []
employees: List[Employee] = []
exams: List[Exam] = []


def get_clinic_by_id(clinic_id: UUID):
    for clinic in clinics:
        if clinic.id == clinic_id:
            return clinic
    return None


def get_employee_by_id(employee_id: UUID):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    return None
