from fastapi import FastAPI
from app.database.db import engine, Base
from app.routers import auth_route, organizations_route, users_route

app = FastAPI(title="API Layer FastAPI ")
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Weelcome FastAPI Application"}

app.include_router(auth_route.router)
app.include_router(organizations_route.router)
app.include_router(users_route.router)
