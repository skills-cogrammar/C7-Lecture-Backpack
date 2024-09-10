import json

class FileAccess:
    def __init__(self, file_name: str):
        self.__file_path = f"resources/{file_name}.json"

    def read(self):
        with open(self.__file_path, "r") as file:
            return json.load(file)            

    def write(self, data: dict):
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    