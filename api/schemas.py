import motor.motor_asyncio
from dotenv import load_dotenv
import os
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client.blog_api

#mongo db uses BSON and fastapi uses JSON
# class to help us convert from bson to json
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectID")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    #__table__ = "user"
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password:str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name":"Vincent Tetteh",
                "email":"vincent@gmail.com",
                "password":"password"
            }
        }


class UserResponse(BaseModel):
    #__table__ = "user"
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId:str}
        schema_extra = {
            "example": {
                "name":"Vincent Tetteh",
                "email":"vincent@gmail.com",
            }
        }


