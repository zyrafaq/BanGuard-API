class InvalidTokenError(Exception):
    def __init__(self, message="Invalid token provided."):
        self.message = message
        super().__init__(self.message)
