import json

from utils.api import GoogleMapsApi
from utils.cheking import Checking

"""Создание, изменение и удаление новой локации"""


class TestCreatePleace():

    def test_create_new_place(self):
        print('Метод POST')
        result_post = GoogleMapsApi.create_new_location()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Метод GET-POST')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        # token = json.loads(result_get.text)
        # print(list(token))

        print('Метод PUT')
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод GET-PUT')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('Метод DELETE')
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('Метод GET-DELETE')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_value(result_get, 'msg', 'Delete operation failed, looks like the data doesn\'t exists')

        print('Тестирование создания, изменения и удаления новой локации прошло успешно!!!')
