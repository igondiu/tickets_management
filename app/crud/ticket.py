
def post_ticket(session, ticket):
    session.add(ticket)
    session.commit()


def put_ticket(session, db_ticket, ticket):
    ticket_data = ticket.model_dump(exclude_unset=True)
    for key, value in ticket_data.items():
        setattr(db_ticket, key, value)

    session.add(db_ticket)
    session.commit()


def close_ticket(session, db_ticket):
    db_ticket.status = "closed"
    session.add(db_ticket)
    session.commit()
