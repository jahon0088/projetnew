from collections import OrderedDict


def formatget(data):
    return OrderedDict({
        'name':data.name,
        "id":data.id,
    })