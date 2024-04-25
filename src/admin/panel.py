from fastapi import FastAPI
from sqladmin import ModelView, Admin
from sqlalchemy import Engine

from config import env_config

from .authentication import AdminAuth
from .dependencies import User

class UserModelView(ModelView, model=User):
    column_list = [
        User.id, 
        User.email, 
        User.registered_at,
    ]
    form_excluded_columns = [
        User.registered_at, 
        User.updated_at,
        User.hashed_password
    ]


def register_admin_views(app: FastAPI, engine: Engine) -> None:
    ''' Register all admin views and make admin object '''

    authentication_backend = AdminAuth(env_config.SQLADMIN_SECRET_KEY)

    admin = Admin(
        app=app,
        engine=engine,
        authentication_backend=authentication_backend
    )

    admin.add_view(UserModelView)



