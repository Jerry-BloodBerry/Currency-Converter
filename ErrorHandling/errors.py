class APIError(Exception):
    def __init__(self, info):
        self.info=info

class UIError(Exception):
    def __init__(self, info):
        self.info=info

class LogicError(Exception):
    def __init__(self, info):
        self.info=info