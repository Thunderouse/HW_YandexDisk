import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload_file(self, loadfile, savefile, replace=False):
        """Загрузка файла.
            savefile: Путь к файлу на Диске
            loadfile: Путь к загружаемому файлу"""
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ""
    file_name = "file"
    yandex_disk_path = f"Test/{file_name}"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload_file(savefile=yandex_disk_path, loadfile=path_to_file)