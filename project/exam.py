from dataclasses import dataclass
from datetime import datetime

from uuid import UUID
from exam_type_enum import ExamTypeEnum


@dataclass
class Exam:
    employee_id: UUID
    clinic_id: UUID
    exam_type: ExamTypeEnum
    start_time: datetime
    end_time: datetime
