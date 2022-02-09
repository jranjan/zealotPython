class RatifierException(Exception):
    _msg = 'Generic Exception'

    def __init__(self):
        pass

    def get_msg(self):
        return self._msg
