import json


def dice(a,b):

    dic = { 'a': a, 'b': b }
    formatted_obj = json.dumps(dic)
    return (formatted_obj)


print(dice(9,10))
