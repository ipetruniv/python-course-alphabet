from pprint import pprint
from copy import deepcopy
from lesson.json_example.json_utils import JsonEncoder, json_hook
import json

#from lesson.some_data import DATA

#
# def show_me(data: dict) -> None:
#     for key, value in data.items():
#         pprint(f"Key {key}; Type : {type(value)}; Value : {value}")


def print_separator() -> None:
    print("\n" * 3)
    print("-" * 20)
def print_dict(somedic: dict):
    print("The dictionary:")
    for k, v in somedic.items():
         print(f"key={k} value={v}, value_type={type(v)}")


if __name__ == "__main__":
    MEMBERS = [
        {'age': 43, 'name': 'Denis'},
        {'age': 49, 'name': 'Roman'},
        {'age': 36, 'name': 'Godzilla'},
        {'age': 47, 'name': 'Spike'},
        {'age': 31, 'name': 'SuperMan'},
        {'age': 49, 'name': 'Batman'},
        {'age': 37, 'name': 'Claus'},
        {'age': 55, 'name': 'Frank'},
        {'age': 83, 'name': 'Homer'}
    ]

    MEMBER = MEMBERS[0]

    DATA = {
        "tuple": tuple(MEMBERS),
        "list": MEMBERS,
        "string": "Json example",
        "integer": 112358,
        "float": 3.14,
        "dict_example": MEMBER
    }

    # Lets see what we have in DATA
    print("GIVEN DATA")
    #show_me(DATA)
    print(type(DATA))

    print_separator()

    # Lets see how json like string will look like
    json_formatted_str = json.dumps(DATA)
    print("JSON formatted string")
    print(type(json_formatted_str), json_formatted_str)
    print_separator()

    # for k, v in DATA.items():
    #     print(f"key={k} value={v}")
    # print_separator()
    # restored_data = eval(json_formatted_str)
    # for k, v in restored_data.items():
    #     print(f"key={k} value={v}")
    # print("Restored data type is: ", type(restored_data))
    # print_separator()
    data2 = deepcopy(DATA)
    data2['set'] = set(range(10))
    print_dict(data2)
    print("Serialized data:")
    serialized_data2 = ""
    try:
        serialized_data2 = json.dumps(data2, cls=JsonEncoder)
    except TypeError as e:
        print(e)
    print(serialized_data2)
    print("Restored data2")
    #restored_data2 = eval(serialized_data2)
    restored_data2 = json.loads(serialized_data2, object_hook=json_hook)
    print_dict(restored_data2)