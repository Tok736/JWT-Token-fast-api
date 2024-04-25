from fastapi import FastAPI

from database import engine

from users.router import router as users_router
from admin.panel  import register_admin_views

def register_routers(app: FastAPI) -> None:
    ''' Register all api routers '''
    
    app.include_router(users_router)

app = FastAPI()

register_routers(app)
register_admin_views(app, engine)