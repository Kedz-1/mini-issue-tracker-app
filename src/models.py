from pydantic import BaseModel
from typing import Optional

class Issue(BaseModel):
    id:Optional[str] = None
    title:str
    description:str
    status:str | None = "Open"

 