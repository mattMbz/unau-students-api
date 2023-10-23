from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.students_router import students_router
from routers.locations_router import locations_router


app = FastAPI()
app.title = "UNAU REST API"
app.version = "1.0.0"

# Globlal middlewares
app.add_middleware(ErrorHandler)

# Routers
app.include_router(students_router)
app.include_router(locations_router)

# Database connections
Base.metadata.create_all(bind=engine)
