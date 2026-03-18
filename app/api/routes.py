from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.openai_service import generate_response
from app.db.database import SessionLocal
from app.db.models import ChatHistory

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    ai_response = generate_response(req.message)

    chat_entry = ChatHistory(
        user_message=req.message,
        ai_response=ai_response
    )

    db.add(chat_entry)
    db.commit()

    return ChatResponse(response=ai_response)
    