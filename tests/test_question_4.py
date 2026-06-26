from src.question_4 import Employee
from datetime import date
import pytest


def test_employee_have_a_start_date_and_end_date_on_job():
    start_date = date(2024, 6, 1)
    end_date = date(2026, 1, 1)

    employee = Employee(start_date=start_date, end_date=end_date, salary=500000)

    assert employee.start_date
    assert employee.days_since_last_work_anniversary == 214
    assert employee.thirteenth_salary_months == 0


def test_employee_have_a_start_date_and_end_date_on_job_with_more_of_15_days():
    start_date = date(2024, 6, 1)
    end_date = date(2026, 1, 16)

    employee = Employee(start_date=start_date, end_date=end_date, salary=500000)

    assert employee.start_date
    assert employee.days_since_last_work_anniversary == 229
    assert employee.thirteenth_salary_months == 1


def test_employee_have_a_termination():
    start_date = date(2024, 6, 1)
    end_date = date(2026, 3, 1)

    employee = Employee(start_date=start_date, end_date=end_date, salary=500000)
    termination = employee.job_termination()

    assert (
        termination.proportional_thirteenth_salary
        == 500000 // 6  # employee.salary / 12 (months year) * 2 (months working)
    )
    assert termination.proportional_paid_leave == round(
        employee.salary * 2 / 3 + 500000 * 1 / 3
    )  # employee.salary / 12 (months year) * 8 (months working) + 1/3 * employee.salary
    assert not employee.active


def test_must_raise_if_employee_has_no_end_date():
    employee = Employee(
        salary=500000,
        start_date=date(2024, 6, 1),
    )

    with pytest.raises(
        ValueError, match="end_date is required for termination calculation"
    ):
        employee.job_termination()


def test_must_return_last_work_anniversary():
    employee = Employee(
        salary=500000,
        start_date=date(2024, 6, 1),
        end_date=date(2026, 3, 15),
    )

    assert employee.last_work_anniversary == date(2025, 6, 1)


def test_must_count_paid_leave_months():
    employee = Employee(
        salary=500000,
        start_date=date(2024, 6, 1),
        end_date=date(2026, 3, 16),
    )

    assert employee.paid_leave_months == 10
