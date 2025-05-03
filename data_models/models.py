import re
from pydantic import BaseModel,field_validator,Field

class DateTimeModel(BaseModel):
    date:str=Field(description="properly formatted date",pattern="^\d{2}-\d{2}-\d{4} \d{2}:\d{2}")

    @field_validator('date')
    def check_format_batch(cls,v):
        if not re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$',v):
            raise ValueError('invaild format')
        return v
class IdentificationNumberModel(BaseModel):
    id:int= Field(description="identification 7 or 8 digits long",pattern="^\d{2}-\d{2}-\d{4}")
    @field_validator("id")
    def check_format_id(cls,v):
        if not re.match(r'^\d{7,8}$',str(v)):\
            raise ValueError('invalid format')
        return v

class DateModel(BaseModel):
    date:str= Field(description="properly formatted date",pattern="^\d{2}-\d{2}-\d{4}")
    @field_validator("date")
    def check_format_id(cls,v):
        if not re.match(r'^\d{2}-\d{2}-\d{4}$',v):
            raise ValueError('invalid format')
        return v
