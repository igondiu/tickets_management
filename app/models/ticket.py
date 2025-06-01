from sqlmodel import SQLModel, Field, Column, Enum
from datetime import datetime


class Ticket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    status: str = Field(
        sa_column=Column(Enum("open", "stalled", "closed", name="ticket_status")),
        default="open"
    )
    created_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"<Ticket(id={self.id}, title='{self.title}', status='{self.status}')>"
