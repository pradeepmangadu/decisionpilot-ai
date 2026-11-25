
from pydantic import BaseModel, Field


class DecisionAnalysis(BaseModel):
    """Structured analysis of a user's decision."""

    decision: str = Field(
        description="Short name of the decision"
    )

    objective: str = Field(
        description="What the user wants to achieve"
    )

    budget: str = Field(
        description="Budget stated by the user, or Not specified"
    )

    requirements: list[str] = Field(
        description="Main requirements for this decision"
    )

    preferences: list[str] = Field(
        description="User's preferences"
    )

    constraints: list[str] = Field(
        description="Limitations or restrictions"
    )

    missing_information: list[str] = Field(
        description="Important details that need clarification"
    )
