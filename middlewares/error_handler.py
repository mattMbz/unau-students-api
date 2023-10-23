from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
    
    #Method for detect errors
    async def dispatch(self, request: Request, call_next) -> Response or JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(
                status_code=500, 
                content = {
                    "Error": str(e),
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
            )