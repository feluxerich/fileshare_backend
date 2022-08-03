from os.path import exists

from fastapi import APIRouter, UploadFile
from starlette.responses import FileResponse, Response

router = APIRouter(tags=['download'])


@router.get('/', response_class=FileResponse, name='file download', description='download a file from the server')
async def download(alias: str):
    if not exists(f'files/{alias}'):
        return Response(status_code=204)
    return FileResponse(f'files/{alias}')
