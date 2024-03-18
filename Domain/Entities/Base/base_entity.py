from datetime import datetime
from typing import Optional
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Column, DateTime, Field, SQLModel, func

class BaseEntity(SQLModel):
    id: Optional[uuid.UUID] = Field(primary_key=True)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now()))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now()))