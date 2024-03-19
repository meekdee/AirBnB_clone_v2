#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker. scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database."""
    __engine = None
    __session = NOne

    def __init__(self):
        """Initializes BDStorage instance."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        models_dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                models_dict[key] = obj

        else:
            for cls in [State, City]:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    models_dict[key] = obj
        return models_dict

    def new(self, obj):
        """Adds new object to storage session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and initializes session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
