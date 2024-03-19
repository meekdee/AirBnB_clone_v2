#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """This class will define all common attributes/methods for
    other classes"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        if not self.id:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """Return string representation"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())

    def __repr__(self):
        """Return string representation"""
        return self.__str__()

    def save(self):
        """Update updated_at attribute"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Delete the instance"""
        models.storage.delete(self)
