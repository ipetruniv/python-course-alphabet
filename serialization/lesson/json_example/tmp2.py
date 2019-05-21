from __future__ import annotations

import json
from typing import Dict, List


class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __str__(self):
        return f"Programmer. Name: {self.name}." \
            f"Lang :{self.language}; Postion: {self.position} developer"

def to_json(obj: Programmer):
    data = {"name": obj.name, "language": obj.language, "position": obj.position}
    return data

def from_json(data):
    return Programmer(name=data['name'], language=data['language'], position=data['position'])


if __name__ == "__main__":
    ourprogramer = Programmer("Vasya")
    print(ourprogramer, type(ourprogramer))
    try:
        json_ourprogramer = json.dumps(ourprogramer)
        print(type(json_ourprogramer))
    except Exception as e:
        print(e)

    try:
        json_ourprogramer2 = json.dumps(ourprogramer, default=to_json)
        print(type(json_ourprogramer2))
        print(json_ourprogramer2)
    except Exception as e:
        print(e)
    #Restore from string
    try:
        restored_ourprogramer = json.loads(json_ourprogramer2)
        print("Restored data:")
        print(type(restored_ourprogramer))
        print(restored_ourprogramer)
    except Exception as e:
        print("Exception:", e)

    try:
        restored_ourprogramer2 = json.loads(json_ourprogramer2, object_hook=from_json)
        print("Restored data2:")
        print(type(restored_ourprogramer2))
        print(restored_ourprogramer2)
    except Exception as e:
        print("Exception:", e)
