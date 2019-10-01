import json
import types

def toLowerCaseSingle(data):
    return {k: v.lower() if isinstance(v, str) else v for k,v in data.items()}

def obtainDict(data):
    keys = list(data.keys())
    for key in keys:
        singleData = data.get(key)        
        if type(singleData)is list:
            for item in singleData:
                item.update(toLowerCaseSingle(item))
        else:
            data.get(key).update(toLowerCaseSingle(singleData))
    return data        