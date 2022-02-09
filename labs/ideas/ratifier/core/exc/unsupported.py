from labs.ideas.ratifier.core.exc.base import RatifierException


class UnsupportedException(RatifierException):
    _msg = 'Unsupported functionality exception'
