from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.analytics_routes import (router as analytics_router)
from app.api.escalation_email_routes import (router as email_router)
from app.core.database import (Base,engine)
from app.models.conversation_memory_model import (ConversationMemory)
from app.models.user_model import User
from app.models.complaint_model import Complaint
from app.models.ticket_model import Ticket
from app.models.escalation_email_model import EscalationEmail
from app.api.memory_routes import (router as memory_router)
from app.services.qdrant_service import (
    QdrantService
)
from app.api.auth_routes import (
    router as auth_router
)

from app.api.complaint_routes import (
    router as complaint_router
)

from app.api.ticket_routes import (
    router as ticket_router
)

from app.api.chat_routes import (
    router as chat_router
)

# -------------------------
# CREATE TABLES
# -------------------------

Base.metadata.create_all(
    bind=engine
)

# -------------------------
# FASTAPI APP
# -------------------------

app = FastAPI()
QdrantService.create_collection()
@app.on_event("startup")
def startup():

    QdrantService.create_collection()
# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -------------------------
# ROUTERS
# -------------------------

app.include_router(auth_router)

app.include_router(
    complaint_router
)
app.include_router(
    email_router
)
app.include_router(
    ticket_router
)

app.include_router(
    chat_router
)
app.include_router(
    analytics_router
)
app.include_router(
    memory_router
)
# -------------------------
# ROOT
# -------------------------

@app.get("/")
def root():

    return {
        "message":
        "Support Ticket SaaS Running"
    }