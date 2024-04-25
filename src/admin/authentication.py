from fastapi import Request
from sqladmin.authentication import AuthenticationBackend

from config import env_config

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        ''' Login to admin panel '''
        form = await request.form()
        username, password = form["username"], form["password"]

        if username == env_config.SQLADMIN_LOGIN.get_secret_value() and password == env_config.SQLADMIN_PASSWORD.get_secret_value():
            request.session.update({"token": "1234"})
            return True
        
        return False

    async def logout(self, request: Request) -> bool:
        ''' Logout from admin panel '''
        request.session.clear()

    async def authenticate(self, request: Request) -> bool:
        ''' Check is user authorized '''
        token = request.session.get("token")

        if not token or token != "1234":
            return False

        return True
