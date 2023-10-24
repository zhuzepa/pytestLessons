import pytest


@pytest.fixture
def set_up():
    print('Вход в систему выполнен')
    yield
    print('Вышли из системы и очистили данные')


def test_send_mail_1(set_up):
    print('Письмо отправлено')


def test_send_mail_2(set_up):
    print('Письмо отправлено')
