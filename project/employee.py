from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class Employee:
    id: UUID
    name: str
    birth: date
    company: str
