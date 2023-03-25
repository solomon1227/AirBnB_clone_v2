#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os

storage_type = getenv(HBNB_TYPE_STORAGE)

if  storage_type == 'db': #import db storage
    from models.engine.file_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else: #import filestorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
