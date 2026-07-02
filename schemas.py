from pydantic import ConfigDict, BaseModel, Field

class PostBase(BaseModel):
  title: str = Field(min_length= 1, max_length= 100)
  content: str = Field(min_length=1)
  author: str = Field(min_length=1,  max_length=50)


class PostCreate(PostBase):
  pass


class PostResponse(PostBase):
  model_config = ConfigDict(from_attributes=True)
  #pydantic by default reads dict but can't read data from objects so by using from_attributes allows
  #use of type notation to access data

  id: int
  date_posted: str
