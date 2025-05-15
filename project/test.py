import unittest
from datetime import datetime, date
from uuid import UUID
from clinic import Clinic, OpeningHours
from employee import Employee
from exam_scheduler import ExamSchedulerClass
from exam_type_enum import ExamTypeEnum
from memory import clinics, employees, exams


class TestExamScheduler(unittest.TestCase):
    def setUp(self):
        clinics.clear()
        employees.clear()
        exams.clear()

        self.clinic = Clinic(
            id=UUID("87654321-4321-8765-4321-567843210987"),
            name="Clinic one",
            exam_types=[ExamTypeEnum.GENERAL_CHECKUP],
            opening_hours=OpeningHours(),
        )

        self.employee = Employee(
            id=UUID("12345678-1234-5678-1234-567812345678"),
            name="Joaquim",
            birth=date(1990, 2, 14),
            company="Google",
        )

        clinics.append(self.clinic)
        employees.append(self.employee)

        self.scheduler = ExamSchedulerClass()

    def test_successful_scheduling(self):
        result = self.scheduler.execute(
            employee_id=self.employee.id,
            clinic_id=self.clinic.id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2023, 10, 16, 14, 0),
        )
        self.assertEqual(result, (True, "Scheduled"))
        self.assertEqual(len(exams), 1)

    def test_outside_opening_hours(self):
        result = self.scheduler.execute(
            employee_id=self.employee.id,
            clinic_id=self.clinic.id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2023, 10, 16, 6, 0),
        )
        self.assertEqual(result, (False, "Examination outside opening hours"))
        self.assertEqual(len(exams), 0)

    def test_schedule_conflict(self):
        self.scheduler.execute(
            employee_id=self.employee.id,
            clinic_id=self.clinic.id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2023, 10, 16, 14, 0),
        )

        result = self.scheduler.execute(
            employee_id=self.employee.id,
            clinic_id=self.clinic.id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2023, 10, 16, 14, 30),
        )
        self.assertEqual(result, (False, "Exam not scheduled due to time conflict"))
        self.assertEqual(len(exams), 1)


if __name__ == "__main__":
    unittest.main()
