from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import Enum as SQLAlchemyEnum


# Define an Enum for the status field
class TicketStatus(str, Enum):
    OPEN = "open"
    STALLED = "stalled"
    CLOSED = "closed"


class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    status: TicketStatus = Field(
        sa_column=Column(SQLAlchemyEnum(TicketStatus), default=TicketStatus.OPEN),
        default=TicketStatus.OPEN
    )
    created_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"<Ticket(id={self.id}, title='{self.title}', status='{self.status}')>"
