import pytest
from employee import Employee


@pytest.fixture
def employee():
    """Karyawan yang tersedia untuk semua fungsi tes."""
    return Employee('eric', 'matthes', 65000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 70000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 75000