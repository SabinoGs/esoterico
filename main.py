from esoterico import __version__ as v
from esoterico.endpoints.user import user_app
from fastapi import FastAPI


app = FastAPI(redoc_url='/', title='Simple API', version=v)
app.include_router(user_app)
