from mongoengine import Document, StringField, EmailField, ListField, ReferenceField, IntField, EmbeddedDocument, EmbeddedDocumentField
from bson import ObjectId

class User(Document):
    username = StringField(max_length=100, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(max_length=100, required=True)

class Team(Document):
    name = StringField(max_length=100, required=True)
    members = ListField(ReferenceField(User))

class Activity(Document):
    activity_id = StringField(default=lambda: str(ObjectId()), unique=True)
    user = ReferenceField(User, required=True)
    activity_type = StringField(max_length=100, required=True)
    duration = StringField(max_length=50, required=True)  # Represent duration as a string

class Leaderboard(Document):
    leaderboard_id = StringField(default=lambda: str(ObjectId()), unique=True)
    user = ReferenceField(User, required=True)
    score = IntField(required=True)

class Workout(Document):
    name = StringField(max_length=100, required=True)
    description = StringField()