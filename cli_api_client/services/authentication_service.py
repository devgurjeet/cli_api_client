class AuthenticationService:
    def __init__(self):
        self.auth_token = ''

    def set_token(self, token):
        self.auth_token = token

    def get_token(self):
        return self.auth_token
