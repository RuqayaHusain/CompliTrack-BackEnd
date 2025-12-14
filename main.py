from fastapi import FastAPI
from controllers.teas import router as TeasRouter
from controllers.comments import router as CommentsRouter
from controllers.users import router as UserRouter

app = FastAPI()

app.include_router(TeasRouter, prefix="/api")
app.include_router(CommentsRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")

@app.get('/')
def home():
    return 'Hello World!'

