import logging
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session, select
from typing import List

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketRead, TicketUpdate
from app.database import get_session
import app.crud.ticket as ticket_crud

router = APIRouter(tags=["tickets"], prefix="/v1")

logger = logging.getLogger(__name__)


@router.post("/tickets/", response_model=TicketRead)
def create_ticket(ticket: TicketCreate, session: Session = Depends(get_session)):
    """Create a new ticket."""
    try:
        db_ticket = Ticket.model_validate(ticket)
        ticket_crud.post_ticket(session, db_ticket)
        return db_ticket
    except Exception as all_e:
        logger.exception(f"An exception occurred while creating ticket: \n{all_e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An exception occurred while creating ticket",
        )


@router.get("/tickets/", response_model=List[TicketRead])
def read_tickets(session: Session = Depends(get_session)):
    """Get all tickets."""
    try:
        tickets = session.exec(select(Ticket)).all()
        return tickets
    except Exception as all_e:
        logger.exception(f"An exception occurred while reading tickets: \n{all_e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An exception occurred while reading tickets",
        )


@router.get("/tickets/{ticket_id}", response_model=TicketRead)
def read_ticket(ticket_id: int, session: Session = Depends(get_session)):
    """Get a specific ticket using its id"""
    try:
        ticket = session.get(Ticket, ticket_id)
        if not ticket:
            return Response(
                status_code=status.HTTP_404_NOT_FOUND,
                content=f"Ticket with id {ticket_id} not found",
                media_type="text/plain",
            )
        return ticket
    except Exception as all_e:
        logger.exception(f"An exception occurred while reading tickets: \n{all_e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An exception occurred while reading tickets",
        )


@router.put("/tickets/{ticket_id}", response_model=TicketRead)
def update_ticket(
    ticket_id: int, ticket: TicketUpdate, session: Session = Depends(get_session)
):
    """Update a specific ticket using its id"""
    try:
        db_ticket = session.get(Ticket, ticket_id)
        if not db_ticket:
            return Response(
                status_code=status.HTTP_404_NOT_FOUND,
                content=f"Ticket with id {ticket_id} not found",
                media_type="text/plain",
            )

        ticket_crud.put_ticket(session, db_ticket, ticket)
        return db_ticket
    except Exception as all_e:
        logger.exception(
            f"An exception occurred while updating ticket with id {ticket_id}: \n{all_e}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An exception occurred while updating ticket with id {ticket_id}",
        )


@router.patch("/tickets/{ticket_id}/close", response_model=TicketRead)
def close_ticket(ticket_id: int, session: Session = Depends(get_session)):
    """Close a specific ticket using its id (ticket's status becomes 'closed')"""
    try:
        db_ticket = session.get(Ticket, ticket_id)
        if not db_ticket:
            return Response(
                status_code=status.HTTP_404_NOT_FOUND,
                content=f"Ticket with id {ticket_id} not found",
                media_type="text/plain",
            )
        ticket_crud.close_ticket(session, db_ticket)
        return db_ticket
    except Exception as all_e:
        logger.exception(
            f"An exception occurred while closing ticket with id {ticket_id}: \n{all_e}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An exception occurred while closing ticket with id {ticket_id}",
        )
