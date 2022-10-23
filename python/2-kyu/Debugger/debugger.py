class Debugger:
    attribute_accesses = []
    method_calls = []


class Meta(type):
    def __new__(mcs, class_name, parents, attributes):
        logged_attributes = {}
        for name, attr in attributes.items():
            logged_attributes[name] = attr
            if callable(attr):
                logged_attributes[name] = logger(mcs, attr)

        logged_attributes['__getattribute__'] = getattr_logger(mcs)
        logged_attributes['__setattr__'] = setattr_logger(mcs)

        return super(Meta, mcs).__new__(mcs, class_name, parents, logged_attributes)


def logger(mcs, func):
    def decorated_func(*args, **kwargs):
        Debugger.method_calls.append({
            'class': mcs,
            'args': args,
            'kwargs': kwargs,
            'method': func.__name__,
        })
        return func(*args, **kwargs)
    return decorated_func


def getattr_logger(mcs):
    def get_logger(self, attr):
        value = object.__getattribute__(self, attr)
        Debugger.attribute_accesses.append({
            'action': 'get',
            'class': mcs,
            'attribute': attr,
            'value': value,
        })
        return value
    return get_logger


def setattr_logger(mcs):
    def set_logger(self, attr, value):
        object.__setattr__(self, attr, value)
        Debugger.attribute_accesses.append({
            'action': 'set',
            'class': mcs,
            'attribute': attr,
            'value': value,
        })
    return set_logger
