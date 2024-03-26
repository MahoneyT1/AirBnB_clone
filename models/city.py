#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ class city for blue print """
    state_id: str = ""
    name: str = ""
