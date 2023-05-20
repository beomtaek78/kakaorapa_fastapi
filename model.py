from pydantic import BaseModel
from typing import List

class Beomtaek(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
                "example": {
                    "id": 1,
                    "item": "Example Schema"
                }
        }

class BeomtaekItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
                "example": {
                "item": "TEST TEST"
        }
    }

class BeomtaekItems(BaseModel):
    beomtaeks: List[BeomtaekItem]

    class Config:
        schema_extra = {
                "example": {
                    "beomtaeks" : [
                        {
                            "item": "Example schema 1"
                        },
                        {
                            "item": "Example schema 2"
                        }
                    ]
                }
        }
