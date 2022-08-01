import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from upload.router import router as upload_router
from download.router import router as download_router
from list.router import router as list_router


def create_app():
    app = FastAPI(
        title="fileshare",
        description="a little filesharing api made by @feluxerich",
        version="0.0.0",
        debug=True,  # TODO: remove debug statement
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.include_router(upload_router, prefix='/upload')
    app.include_router(download_router, prefix='/download')
    app.include_router(list_router, prefix='/list')

    @app.get("/", name='Index, redirects to openapi docs')
    async def root():
        return RedirectResponse(url='/docs')

    return app


if __name__ == "__main__":
    uvicorn.run(create_app())
