from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.models.ticket import TicketStatus


class TicketBase(BaseModel):
    title: str
    description: str
    status: TicketStatus = Field(default=TicketStatus.OPEN)


class TicketCreate(TicketBase):
    pass


class TicketRead(TicketBase):
    id: int
    created_at: datetime


class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TicketStatus] = None
