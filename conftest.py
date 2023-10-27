import pytest


@pytest.fixture
def set_up():
    print('Вход в систему выполнен')
    yield
    print('Вышли из системы и очистили данные')
