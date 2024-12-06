from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import your API routes
from api.user_api import user_router
from api.auth_api import auth_router
from api.product_api import router

# Initialize FastAPI app
app = FastAPI(
    title="LMS", docs_url="/api/docs", openapi_url="/api"
)

# Include user API router
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(router)

# Configure CORS
origins = ["*"]  # Set allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for database session handling
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    # Example: Uncomment and modify the below lines if you use a database session
    # request.state.db = SessionLocal()  # Add DB session to request state
    response = await call_next(request)
    # request.state.db.close()  # Clean up the DB session
    return response

# Root endpoint for health check or welcome message
@app.get("/")
async def read_root():
    return {"message": "Welcome to the LMS API!"}
