from fastapi import FastAPI  # Depends, Header, HTTPException

from .routers import simple_get, demo_config

app = FastAPI()

app.include_router(
    demo_config.router,
    prefix="/config",
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    simple_get.router,
    prefix="/simple",
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)