from fastapi import FastAPI
from app.core.database import (Base,engine)
from app.models.user_model import User
from app.models.complaint_model import Complaint
from app.models.ticket_model import Ticket
from app.models.escalation_email_model import EscalationEmail
from app.api.auth_routes import (router as auth_router)
from app.api.auth_routes import (router as auth_router)
from app.api.complaint_routes import (router as complaint_router)
from app.api.ticket_routes import (router as ticket_router)
from app.api.chat_routes import (router as chat_router)


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_router)
app.include_router(complaint_router)
app.include_router(ticket_router)
app.include_router(chat_router)

@app.get("/")
def root():

    return {
        "message": "Support Ticket SaaS Running"
    }