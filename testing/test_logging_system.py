import os
import pytest
from my_hairdressing_app.config import Config
from my_hairdressing_app.normal_haircut import NormalHaircut
from my_hairdressing_app.appointment_schedule_manager import AppointmentScheduleManager

DAY = '13-12-2021'
SHIFT = 'MORNING'

@pytest.fixture
def schedule_manager():
    return AppointmentScheduleManager(test = True)

@pytest.fixture
def normal_haircut():
    return NormalHaircut()
    
@pytest.fixture
def logging_config():
    return Config(test = True).get_logging_config()


def test_logger(logging_config, schedule_manager, normal_haircut):
    """
    Test para comprobar que se registra un log a los distintos niveles especificados.
    """

    schedule_manager.book_appointment('13122021', SHIFT, normal_haircut)
    schedule_manager.book_appointment(DAY, SHIFT, normal_haircut)

    file_name = logging_config['handlers']['file']['filename']
    print(file_name)
    with open(file_name) as file:
        file_content = file.read()
        if not 'INFO' in file_content and not 'CRITICAL' in file_content:
            assert False

    # Borramos el contenido del archivo de log     
    os.remove(file_name)
    
    assert True
