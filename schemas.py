from pydantic import BaseModel, Field
from typing import Literal

class ChatResponse(BaseModel):
    answer : str = Field(description="The main answer to the user's question")
    
    summary : str = Field(description="A short summary of the answer")
    
    category : Literal["programming", "mathematics", "general"] = Field(description="The category of the user's question")
    
    confidence: float = Field(
        description="Confidence in the answer from 0 to 1",
        ge=0,
        le=1
    )
    
    keywords : list[str] = Field(description="Important keywords related to the answer")