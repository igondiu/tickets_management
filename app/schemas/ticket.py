from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


# Define an Enum for the status field
class TicketStatus(str, Enum):
    open = "open"
    stalled = "stalled"
    closed = "closed"


class TicketBase(SQLModel):
    title: str
    description: str
    status: TicketStatus = Field(default=TicketStatus.open)


class TicketCreate(TicketBase):
    pass


class TicketRead(TicketBase):
    id: int
    created_at: datetime


class TicketUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TicketStatus] = None
