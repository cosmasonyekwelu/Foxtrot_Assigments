import json


class Model:
    @staticmethod
    def save_a_file(name_of_file, content):
        with open(name_of_file, "w") as store:
            convert_to_json = json.dumps(content, indent=4)
            store.write(convert_to_json)

    @staticmethod
    def load_a_file(name_of_file):
        try:
            with open(name_of_file) as store:
                content = json.loads(store.read())
                return content
        except FileNotFoundError:
            return []
