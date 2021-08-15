from fastapi_jwt_auth import AuthJWT
from decouple import config
from Database.Database import get_db
from Database.models import models
from pydantic import BaseModel

class Settings(BaseModel):
    authjwt_secret_key: str = config("SECRET")
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access","refresh"}

@AuthJWT.load_config
def get_config():
    return Settings()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    db = next(get_db())
    exists = db.query(models.AuthResponsableToken).filter(
            models.AuthResponsableToken.jti == decrypted_token.get("jti"),
            models.AuthResponsableToken.status == 1
            ).first()
    return False if exists else True
    