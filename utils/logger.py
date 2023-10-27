import datetime
import os


class Logger():
    file_name = f'logs/log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

    @classmethod
    def write_log_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_requests(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = '\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {datetime.datetime.now()}\n'
        data_to_add += f'Requests METHOD: {method}\n'
        data_to_add += f'Requests URL: {url}\n'
        data_to_add = '\n'

        cls.write_log_file(data_to_add)

    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f'Response code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'
        data_to_add += '\n-----\n'

        cls.write_log_file(data_to_add)
