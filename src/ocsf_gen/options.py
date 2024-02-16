from pydantic import BaseModel, DirectoryPath


class Options(BaseModel):
    path: DirectoryPath