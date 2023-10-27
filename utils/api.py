from urllib.parse import urljoin

from utils.http_method import HttpMethods

"""Методы для тестирования Google maps API"""
BASE_URL = 'https://rahulshettyacademy.com'
PARAMS = '?key=qaclick123'
POST_RESOURCE = '/maps/api/place/add/json'  # Ресурс метода POST
GET_RESOURCE = '/maps/api/place/get/json'  # Ресурс метода GET
PUT_RESOURCE = '/maps/api/place/update/json'  # Ресурс метода PUT
DELETE_RESOURCE = '/maps/api/place/delete/json' # Ресурс метода DELETE


class GoogleMapsApi():
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_location():
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = BASE_URL + POST_RESOURCE + PARAMS
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_url = BASE_URL + GET_RESOURCE + PARAMS + '&place_id=' + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для удаления новой локации"""
    @staticmethod
    def put_new_place(place_id):
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_url = BASE_URL + PUT_RESOURCE + PARAMS
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        json_for_delete_new_location = {
            "place_id": place_id
     }
        del_url = BASE_URL + DELETE_RESOURCE + PARAMS
        print(del_url)
        result_del = HttpMethods.delete(del_url, json_for_delete_new_location)
        print(result_del.text)
        return result_del

