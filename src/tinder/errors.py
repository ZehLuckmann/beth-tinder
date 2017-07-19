class TinderError(Exception):
    pass


class RequestError(TinderError):
    pass


class InitializationError(TinderError):
    pass


class RecsError(TinderError):
    pass


class RecsTimeout(RecsError):
    pass
