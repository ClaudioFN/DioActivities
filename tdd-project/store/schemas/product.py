import datetime
from decimal import Decimal
from typing import Annotated, Optional
import uuid
from bson import Decimal128
from pydantic import UUID4, AfterValidator, BaseModel, Field, model_validator
from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product Name")
    quantity: int = Field(..., description="Product Quantity")
    price: Decimal = Field(..., description="Product Price")
    status: bool = Field(..., description="Product Status")

class ProductIn(ProductBase, BaseSchemaMixin):
    ...

class ProductOut(ProductIn, OutSchema):
    ...
    #id: UUID4 = Field()
    #created_at: datetime = Field()
    #update_at: datetime = Field()
    #
    #@model_validator(mode="before")
    #def set_schema(cls, data):
    #    for key, value in data.items():
    #        if isinstance(value, Decimal128):
    #            data[key] = Decimal(str(value))
    #
    #    return data
    
def convert_decimal_128(v):
    return Decimal128(str(v))

Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]

class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product Quantity")
    price: Optional[Decimal_] = Field(None, description="Product Price")
    status: Optional[bool] = Field(None, description="Product Status")
    
class ProductUpdateOut(ProductOut):
    ...