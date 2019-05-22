import json


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
            # Let the base class default method raise the TypeError
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def json_hook(obj):
    # newobj = dict({})
    # for k, v in obj.items():
    #     if k == 'set':
    #         newobj[k] = set(v)
    #     else:
    #         newobj[k] = v
    # return newobj
    return {k: (set(v) if k == 'set' else v) for (k, v) in obj.items()}