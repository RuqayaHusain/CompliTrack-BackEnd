from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.users import router as UserRouter
from controllers.businesses import router as BusinessesRouter
from controllers.licenses import router as LicensesRouter
from controllers.compliance_tasks import router as ComplianceTasksRouter

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(UserRouter, prefix="/api/auth")
app.include_router(BusinessesRouter, prefix="/api", tags=["Businesses"])
app.include_router(LicensesRouter, prefix="/api", tags=["Licenses"])
app.include_router(ComplianceTasksRouter, prefix="/api", tags=["Compliance Tasks"])

@app.get('/')
def home():
    return {'message': 'Welcome to CompliTrack API! Visit /docs for API documentation.'}

