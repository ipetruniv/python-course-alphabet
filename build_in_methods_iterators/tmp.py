
given_data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
              {'age': 49, 'name': 'Roman', 'sex': 'male'},
              {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
              {'age': 47, 'name': 'spike', 'sex': 'female'},
              {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
              {'age': 49, 'name': 'Batman', 'sex': 'male'},
              {'age': 37, 'name': 'claus', 'sex': 'male'},
              {'age': 55, 'name': 'Frank', 'sex': 'female'},
              {'age': 83, 'name': 'homer', 'sex': 'male'}
              ]
def task_3_find_item_via_value(data, value):

    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for key in redundant_keys:
        for item in data:
            if key in item:
                del item[key]

    return [rdata for rdata in data if value in rdata.values()]
value_to_search = 'SuperMan'
expected_result = [{'age': 31, 'name': 'SuperMan', 'sex': 'female'}]
print(task_3_find_item_via_value(data=given_data, value=value_to_search))

