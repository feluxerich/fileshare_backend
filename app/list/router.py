from os import listdir, path
from typing import List

from fastapi import APIRouter, UploadFile

from app.utils import to_alias, from_alias, get_filesize
from .schemas import ListedFile

router = APIRouter(tags=['list'])


@router.get('/', response_model=List[ListedFile], name='list all', description='list all saved files')
async def list_all():
    return [{
        'filename': from_alias(file),
        'filesize': get_filesize(f'files/{file}'),
        'alias': file} for file in listdir('files/')]
