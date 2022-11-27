from fastapi import FastAPI
from ecom.auth import router as auth_router
from ecom.user import router as user_router

app = FastAPI()


app.include_router(auth_router.router)
app.include_router(user_router.router)
