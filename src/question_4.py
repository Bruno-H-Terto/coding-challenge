from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class Termination:
    """Represents the calculated termination payments."""

    proportional_thirteenth_salary: int
    proportional_paid_leave: int


@dataclass(slots=True)
class Employee:
    """Represents an employee and calculates termination-related payments."""

    salary: int
    start_date: date
    active: bool = True
    end_date: date | None = None
    termination: Termination | None = None

    def _ensure_terminated(self) -> date:
        if self.end_date is None:
            raise ValueError("end_date is required for termination calculation")

        return self.end_date

    def _count_proportional_months(self, start: date, end: date) -> int:
        """Count months with at least 15 worked days between two dates."""
        months = 0
        current = date(start.year, start.month, 1)

        while current <= end:
            next_month = date(
                current.year + (current.month == 12),
                1 if current.month == 12 else current.month + 1,
                1,
            )

            month_start = max(start, current)
            month_end = min(end, next_month)

            if (month_end - month_start).days >= 15:
                months += 1

            current = next_month

        return months

    @property
    def last_work_anniversary(self) -> date:
        end_date = self._ensure_terminated()
        anniversary = self.start_date.replace(year=end_date.year)

        if anniversary > end_date:
            anniversary = anniversary.replace(year=end_date.year - 1)

        return anniversary

    @property
    def days_since_last_work_anniversary(self) -> int:
        end_date = self._ensure_terminated()

        return (end_date - self.last_work_anniversary).days

    @property
    def thirteenth_salary_months(self) -> int:
        end_date = self._ensure_terminated()
        first_day_of_year = date(end_date.year, 1, 1)

        return self._count_proportional_months(first_day_of_year, end_date)

    @property
    def paid_leave_months(self) -> int:
        end_date = self._ensure_terminated()

        return self._count_proportional_months(self.last_work_anniversary, end_date)

    def job_termination(self) -> Termination:
        thirteenth_salary = self.salary * self.thirteenth_salary_months // 12

        paid_leave_base = self.salary * self.paid_leave_months // 12
        paid_leave_bonus = paid_leave_base // 3

        self.termination = Termination(
            proportional_thirteenth_salary=thirteenth_salary,
            proportional_paid_leave=paid_leave_base + paid_leave_bonus,
        )
        self.active = False

        return self.termination
