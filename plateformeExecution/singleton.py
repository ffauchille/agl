__author__ = 'flo'


class Singleton(type):
    """
        Singleton implementation
        usage :

        class MyClass(BaseClass):
            __metaclass__ = Singleton

            ...
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]