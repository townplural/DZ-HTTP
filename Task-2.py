import requests
# from TOKEN import TOKEN
from pprint import pprint


class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        pprint(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            pprint('Загрузка прошла успешно!')


ya = Yandex(TOKEN)
file_path = input('Введите путь до фаила')
ya.upload_to_disk(f'{file_path}', yandex_path='/Test/hello_Yandex.txt')
