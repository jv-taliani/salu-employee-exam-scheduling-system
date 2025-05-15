from dataclasses import dataclass, field
from datetime import datetime, time
from typing import Optional
from uuid import UUID
from project.exam_type_enum import ExamTypeEnum


@dataclass
class OpeningHours:
    working_hours: dict[int, Optional[tuple[str, str]]] = field(
        default_factory=lambda: {
            0: ("07:00", "17:00"),
            1: ("07:00", "17:00"),
            2: ("07:00", "17:00"),
            3: ("07:00", "17:00"),
            4: ("07:00", "17:00"),
            5: None,
            6: None,
        }
    )


@dataclass
class Clinic:
    id: UUID
    name: str
    exam_types: list[ExamTypeEnum]
    opening_hours: OpeningHours

    def offers_exam(self, exam_type: ExamTypeEnum) -> bool:
        return exam_type in self.exam_types

    def operation_week(self, dt: datetime) -> bool:
        weekday = dt.weekday()
        return self.opening_hours.working_hours.get(weekday) is not None

    def operation_time(self, dt: datetime) -> bool:
        weekday = dt.weekday()
        hours = self.opening_hours.working_hours.get(weekday)
        if not hours:
            return False
        start, end = map(time.fromisoformat, hours)
        return start <= dt.time() < end
