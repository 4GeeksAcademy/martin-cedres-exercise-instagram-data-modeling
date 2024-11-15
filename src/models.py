import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Aquí definimos columnas para tabla person
    # Observe que cada columna también es un atributo de instancia normal de Python.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Aquí definimos columnas para la dirección de la tabla.
    # Observe que cada columna también es un atributo de instancia normal de Python.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base): 
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(50), nullable=False, unique=True)
    coments = relationship('Coment', back_populates="author_id_relationship")  # relationship con 'coments' representa el UNO 
    posts = relationship('Post', back_populates="user_id_relationship")   # relationship con 'posts', representa el UNO
    follower = relationship('follower', back_populates="user_to_relationship") # relacion con follower, representa el UNO 

class Coment(Base):
    __tablename__= 'coment'
    id = Column(Integer, primary_key=True)
    coment_text = Column(String(300), nullable=False)#campo obligatorio
    author_id = Column(Integer, ForeignKey('user.id'))#Clave foranea representa el MUCHOS (un usuario puede tener muchos comntarios)
    author_id_relationship = relationship('User', back_populates='coments')
    
class Post(Base): 
    __tablename__= 'post'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))#clave foranea a usar ue representa "muchos"
    user_id_relationship = relationship('User', back_populates='posts')#relacion con User
    media = relationship('Media', back_populates='post_id_relationship')

class Media(Base): 
    __tablename__='media' 
    id=Column(Integer, primary_key=True)
    type= Column()
    url= Column(String(50))
    post_id= Column(Integer, ForeignKey('post.id'))#Clave foranea MUCHOS a un POST
    post_id_relationship = relationship ('Post', back_populates='media')
    
#ME FALTA ESTABLECER LA RELACION MUCHOS A UNO ENTRE FOLLOWER Y USER
class Follower(Base): 
    __tablename__='follower'
    id = Column(Integer, primary_key=True)  # Clave primaria simple para el follower
    user_form_id = Column (Integer, ForeignKey('user.id')) # El uruario que sigue
    user_to_id = Column (Integer, ForeignKey('user.id')) # El usuario que es seguido
    user_to_id_relationship = relationship ('User', back_populates='follower')



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
