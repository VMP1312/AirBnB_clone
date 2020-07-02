#!/usr/bin/python3
"""
Review class
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Review class"""
    text = ""
    user_id = ""
    place_id = ""