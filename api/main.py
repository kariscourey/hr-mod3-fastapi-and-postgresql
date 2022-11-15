from fastapi import FastAPI
from routers import vacations


app = FastAPI() # create app
app.include_router(vacations.router) # include routers
