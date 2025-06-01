"""This module contains tests for the ticket module in routers directory."""

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models.ticket import Ticket


def test_create_ticket_fails(client: TestClient):
    test_ticket = {
        "title": "Test Ticket",
        "description": "This is a test ticket.",
        "status": "other",
    }
    response = client.post(
        "/v1/tickets/",
        json=test_ticket,
    )
    assert 399 < response.status_code < 499, "A client error must be detected"


def test_create_ticket(client: TestClient):
    test_ticket = {"title": "Test Ticket", "description": "This is a test ticket."}
    response = client.post(
        "/v1/tickets/",
        json=test_ticket,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == test_ticket["title"]
    assert data["description"] == test_ticket["description"]


def test_read_tickets(client: TestClient, session: Session):
    ticket = Ticket(title="Test Ticket", description="This is a test ticket.")
    session.add(ticket)
    session.commit()

    response = client.get("/v1/tickets/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_read_unexisting_ticket(client: TestClient):
    response = client.get(f"/v1/tickets/-1")
    assert response.status_code == 404, "Such ticket must not exist"


def test_read_ticket(client: TestClient, session: Session):
    ticket = Ticket(title="Test Ticket", description="This is a test reading ticket.")
    session.add(ticket)
    session.commit()

    response = client.get(f"/v1/tickets/{ticket.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Ticket"


def test_update_ticket_failed(client: TestClient, session: Session):
    ticket = Ticket(title="Test Ticket", description="This is a test ticket.")
    session.add(ticket)
    session.commit()

    response = client.put(
        f"/v1/tickets/{ticket.id}",
        json={
            "title": "Updated Ticket",
            "description": "This is an updated ticket.",
            "status": "other",
        },
    )
    assert 399 < response.status_code < 499, "A client error must be detected"


def test_update_ticket(client: TestClient, session: Session):
    ticket = Ticket(title="Test Ticket", description="This is a test ticket.")
    session.add(ticket)
    session.commit()

    updated_ticket_body = {
        "title": "Updated Ticket",
        "description": "This is an updated ticket.",
        "status": "stalled",
    }

    response = client.put(
        f"/v1/tickets/{ticket.id}",
        json=updated_ticket_body,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_ticket_body["title"]
    assert data["description"] == updated_ticket_body["description"]
    assert data["status"] == updated_ticket_body["status"]


def test_close_ticket_fails(client: TestClient, session: Session):
    response = client.patch(
        f"/v1/tickets/{-1}/close"
    )
    assert response.status_code == 404, "Such ticket must not be found"


def test_close_ticket(client: TestClient, session: Session):
    ticket = Ticket(title="Test Ticket", description="This is a test ticket.")
    session.add(ticket)
    session.commit()

    response = client.patch(f"/v1/tickets/{ticket.id}/close")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "closed"
