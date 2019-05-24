import uuid


uuid_str = uuid.uuid4()
print(str(uuid_str))
print(uuid_str.urn[9:])

