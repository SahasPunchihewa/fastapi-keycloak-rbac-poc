from fastapi import FastAPI, Header
from keycloak_auth.keycloak_auth import KeycloakAuth

from settings import KEYCLOAK_URL, KEYCLOAK_CLIENT_ID, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_SECRET

app = FastAPI()

auth: KeycloakAuth = KeycloakAuth(server_url=KEYCLOAK_URL,
                                  client_id=KEYCLOAK_CLIENT_ID,
                                  realm_name=KEYCLOAK_REALM_NAME,
                                  client_secret_key=KEYCLOAK_CLIENT_SECRET,
                                  use_resource_access=True)


@app.get('/admin')
@auth.RolesAllowed(['admin'])
async def admin_rote(authorization: str | None = Header(default=None)):
    return {'message': 'Hello Admin'}


@app.get('/user')
@auth.RolesAllowed(['admin', 'user'])
async def admin_rote(authorization: str | None = Header(default=None)):
    return {'message': 'Hello User'}
