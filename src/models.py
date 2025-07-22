from pydantic import BaseModel
from typing import Optional

class Issue(BaseModel):
    id:Optional[str] = None
    title:str
    description:str
    status:str | None = "Open"

 
class Patch(BaseModel):
   id:Optional[str] = None
   title:Optional[str] = None
   description:str = None
   status:str | None = "Open"