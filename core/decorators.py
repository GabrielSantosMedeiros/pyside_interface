
def singleton(cls):
    _instances = {}
    def check(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return check
