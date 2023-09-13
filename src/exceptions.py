class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InstantiateCSVError(Exception):
    def __init__(self, message):
        super().__init__(message)