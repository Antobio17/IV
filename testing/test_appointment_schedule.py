import pytest
from my_hairdressing_app.errors import BadDateFormatError 
from my_hairdressing_app.errors import ShiftNotExistError
from my_hairdressing_app.appointment_schedule import AppointmentSchedule
from my_hairdressing_app.normal_haircut import NormalHaircut

DAY = '14-11-2021'
SHIFT = 'MORNING'

@pytest.fixture
def appointments():
    return AppointmentSchedule()

@pytest.fixture
def normal_haircut():
    return NormalHaircut()


def test_can_book_appointment(appointments, normal_haircut):
    """
    Test para comprobar que, cuando hay un hueco en el día y turno seleccionado, se puede reservar una cita.
    """
    assert appointments.book_appointment(DAY, SHIFT, normal_haircut, test = True) == True


def test_can_not_book_appointment(appointments, normal_haircut):
    """
    Test para comprobar que, cuando no hay hueco en el día y turno seleccionado, no se puede reservar una cita.

    Se completará el turno de un día y se probará a realizar una insercción de una cita
    """
    count = 0
    while count < 300:
        appointments.book_appointment(DAY, SHIFT, normal_haircut)
        count += normal_haircut.getDuration()['first_working_step']

    assert appointments.book_appointment(DAY, SHIFT, normal_haircut, test = True) == False


def test_expected_exception_atribute_date(appointments, normal_haircut):
    """
    Test para comprobar el levantamiento de excepciones cuando no se introduce correctamente la fecha en la reserva de cita.
    """
    with pytest.raises(BadDateFormatError, match = r".* fecha .*"):
        appointments.book_appointment('14112021', SHIFT, normal_haircut, test = True)


def test_expected_exception_atribute_shift(appointments, normal_haircut):
    """
    Test para comprobar el levantamiento de excepciones cuando no se introduce correctamente el turno de trabajo en la reserva de cita.
    """
    with pytest.raises(ShiftNotExistError, match = r".* turno .*"):
        appointments.book_appointment(DAY, 'm', normal_haircut, test = True)
