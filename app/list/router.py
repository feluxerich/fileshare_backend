from os import listdir, path
from typing import List

from fastapi import APIRouter, UploadFile

from .schemas import ListedFile

router = APIRouter(tags=['list'])


@router.get('/', response_model=List[ListedFile], name='list all', description='list all saved files')
async def list_all():
    return [{'filename': file, 'filesize': path.getsize(f'files/{file}')} for file in listdir('files/')]
