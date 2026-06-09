from fastapi import APIRouter
from fastapi import Depends
from app.services.qdrant_memory_service import (
    QdrantMemoryService
)
from sqlalchemy.orm import Session
from app.services.followup_llm_service import (
    FollowupLLMService
)


from app.core.database import get_db

from app.schemas.chat_schema import (
    ChatRequest
)

from app.services.memory_service import (
    MemoryService
)

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.orchestrators.langgraph_orchestrator import (
    LangGraphOrchestrator
)


from app.services.followup_agent_service import (
    FollowupAgentService
)
router = APIRouter(
    prefix="/api/chat",
    tags=["AI Chat"]
)


@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    # Save User Message

    MemoryService.save_message(
        db=db,
        user_id=current_user.id,
        role="user",
        content=request.message
    )
    
   

    

    
    # Process AI Workflow
    QdrantMemoryService.save_memory(

    user_id=current_user.id,

    role="user",

    content=request.message
)
    result = (
        LangGraphOrchestrator.process(
            message=request.message,
            user_id=current_user.id,
            db=db
        )
    )
    QdrantMemoryService.save_memory(

    user_id=current_user.id,

    role="assistant",

    content=result.get("response"),

    ticket_id=
    result.get("ticket_id"),

    complaint_id=
    result.get("complaint_id")
)

    # Save Assistant Response

    MemoryService.save_message(
        db=db,
        user_id=current_user.id,
        role="assistant",
        content=result.get("response")
    )

    return {
        "message": request.message,

        "is_complaint":
            result.get("is_complaint"),

        "category":
            result.get("category"),
  
        "priority":
            result.get("priority"),

        "complaint_exists":
            result.get("complaint_exists"),

        "complaint_id":
            result.get("complaint_id"),

        "ticket_id":
            result.get("ticket_id"),

        "response":
            result.get("response")
    }