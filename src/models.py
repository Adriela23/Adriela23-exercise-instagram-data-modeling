import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Enum, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

db = SQLAlchemy()


class Follower(db.Model):
    id = Column(Integer, primary_key=True)

    user = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)
    

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    comment = Column(String(255), nullable=False)

    user = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    description = Column(String(255))

    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)


class Type (enum.Enum):
    video= 1
    image= 2
    img_set= 3

class Media(db.Model):
    id = Column(Integer, primary_key=True)
    url= Column(String(255), nullable=False)
    type = Column(Enum(Type), nullable=False)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base 
try:
    result = render_er(db.Model, './img/diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
