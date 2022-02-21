class ReconcilerException(Exception):
    """Represents base class for all error."""

    def __init__(self):
        self._msg = "void"
        self._ec = 0

    def __repr__(self):
        return 'BaseException(msg={msg}, code={code}'.format(msg=self._msg, code=self._ec)

    def __str__(self):
        return '!!!!! Error(message={msg}, code={code}) !!!!!'.format(msg=self._msg, code=self._ec)

    def get(self):
        return {'msg': self._msg, 'code': self._ec}
