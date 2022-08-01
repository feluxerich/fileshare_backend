from pydantic import BaseModel


class ListedFile(BaseModel):
    filename: str
    filesize: int
    alias: str
