from fastapi import APIRouter, UploadFile

from .schemas import Upload

router = APIRouter(tags=['upload'])


@router.post('/', response_model=Upload, name='file upload', description='upload a file to the server')
async def upload(file: UploadFile):
    with open(f'files/{file.filename}', 'wb') as f:
        contents = await file.read()
        f.write(contents)
    return {'filename': file.filename}
