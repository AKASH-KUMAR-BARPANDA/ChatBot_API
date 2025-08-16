from ROUTERS import ROUTES
from fastapi import FastAPI

app = FastAPI()


app.include_router(ROUTES.router) # first the file name then the api-routes name