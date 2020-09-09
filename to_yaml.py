import yaml
from functools import wraps


def to_yaml(func):
    @wraps(func)
    def wrapper(*args):
        result = yaml.dump(func(*args))
        print(result)
        return result
    return wrapper
