__author__ = 'Evren Esat Ozkan'


class DotDict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
