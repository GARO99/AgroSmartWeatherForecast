from decimal import Decimal
from Domain.Entities.Base.base_entity import BaseEntity
from sqlmodel import Field


class FarmerLand(BaseEntity, table=True):
    name: str = Field(default=None, nullable=False)
    longitude: Decimal =  Field(default=None, nullable=False)
    latitude: Decimal =  Field(default=None, nullable=False)