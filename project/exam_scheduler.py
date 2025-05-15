from datetime import datetime, timedelta
from uuid import UUID
from exam import Exam
from memory import get_clinic_by_id, get_employee_by_id, exams
from exam_type_enum import ExamTypeEnum


class ExamSchedulerClass:
    def execute(
        self,
        employee_id: UUID,
        clinic_id: UUID,
        exam_type: ExamTypeEnum,
        exam_start: datetime,
    ) -> tuple[bool, str]:
        clinic = get_clinic_by_id(clinic_id)
        if not clinic:
            return False, "clinic not found"

        employee = get_employee_by_id(employee_id)
        if not employee:
            return False, "Employee not found"

        if not clinic.offers_exam(exam_type):
            return False, "The clinic does not offer this exam."

        if not clinic.operation_week(exam_start):
            return False, "The clinic is closed on this day of the week"

        if not clinic.operation_time(exam_start):
            return False, "Examination outside opening hours"

        exam_end = exam_start + timedelta(hours=1)

        for sheduled_exam in exams:
            if sheduled_exam.clinic_id != clinic_id:
                continue
            if (
                exam_start < sheduled_exam.end_time
                and exam_end > sheduled_exam.start_time
            ):
                return False, "Exam not scheduled due to time conflict"

        new_exam = Exam(
            employee_id=employee_id,
            clinic_id=clinic_id,
            exam_type=exam_type,
            start_time=exam_start,
            end_time=exam_end,
        )

        exams.append(new_exam)
        return True, "Scheduled"
