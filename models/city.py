#!/usr/bin/python3
"""
City class
"""
from models.base_model import BaseModel
from models.state import State
import models


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""
