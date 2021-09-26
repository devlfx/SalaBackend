from fastapi import FastAPI,Depends, Request,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.openapi.utils import get_openapi
from responsables.router import router as responsablesRouter
from decouple import config
from responsables.Services import Utilities
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()




@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    print("token",request.headers)
    print("path",request.url.path)
    print("url",request.url)
    print("schema", request.url.scheme)
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )




app.include_router(
        responsablesRouter,
        prefix="",
        tags=["users"]
    )


def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="SEVi",
        version="2.5.0",
        description="API Documentation",
        routes=app.routes,
    )

    # Custom documentation fastapi-jwt-auth
    headers = {
        "name": "Authorization",
        "in": "header",
        "required": True,
        "schema": {
            "title": "Authorization",
            "type": "string"
        },
    }
    
    # Get routes from index 4 because before that fastapi define router for /openapi.json, /redoc, /docs, etc
    # Get all router where operation_id is authorize
    router_authorize = [route for route in app.routes[4:] if "Autheticated" in route.tags]

    for route in router_authorize:

        method = list(route.methods)[0].lower()
        try:
            # If the router has another parameter
            openapi_schema["paths"][route.path][method]['parameters'].append(headers)
        except Exception:
            # If the router doesn't have a parameter
            openapi_schema["paths"][route.path][method].update({"parameters":[headers]})

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi