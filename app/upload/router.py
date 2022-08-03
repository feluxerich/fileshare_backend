from fastapi import APIRouter, UploadFile

from .schemas import Upload
from app.utils import to_alias

router = APIRouter(tags=['upload'])


@router.post('/', response_model=Upload, name='file upload', description='upload a file to the server')
async def upload(file: UploadFile):
    contents = await file.read()
    with open(f'files/{to_alias(file.filename)}.{len(contents)}', 'wb') as f:
        f.write(contents)
    return {'filename': file.filename, 'alias': f'{to_alias(file.filename)}.{len(contents)}'}
