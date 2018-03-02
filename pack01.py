import struct
import json

person={"姓名":"中国人","性别":"男","年龄":80}
print("person:",person)
json_person=json.dumps(person)
print("json_person:",json_person)
encode_json_person=json_person.encode()
print("encode_json_person:",encode_json_person)
pack_encode_json_person=struct.pack("{}s".format(len(encode_json_person)),encode_json_person)
print("pack_encode_json_person:",pack_encode_json_person)
unpack_encode_json,=struct.unpack("{}s".format(len(pack_encode_json_person)),pack_encode_json_person)
print("unpack_encode_json:",unpack_encode_json)
recover_person=json.loads(unpack_encode_json.decode())
print("recover_person:",type(recover_person),recover_person)
print("*"*30)
print("person:",person)
str_person=str(person)
print("str_person:",str_person)
encode_str_person=str_person.encode()
print("encode_str_person:",encode_str_person)
pack_encode_str_person=struct.pack("{}s".format(len(encode_str_person)),encode_str_person)
print("pack_encode_str_person:",pack_encode_str_person)
recover_person=eval(encode_str_person.decode())
print("recover_person:",type(recover_person),recover_person)