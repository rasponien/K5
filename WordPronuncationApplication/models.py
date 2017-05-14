from django.db import models
from mongoengine import *
from gridfs import GridFS


class Word(Document):
    word = StringField(max_length=255, required=True)
    pronunciation = FileField()
