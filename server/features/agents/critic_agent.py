from .config.models import google_model
from pydantic_ai import Agent
from pydantic import BaseModel, Field

# Output format
class Critic(BaseModel):
    validated_findings: list[str] = Field(
        description="This is the list of all the validated findings."
    )
    false_findings: list[str] = Field(
        description="This is a list of findings that were invalid, or fake."
    )

# The critic agent
agent = Agent(
    name="Critic Agent",
    model=google_model,
    system_prompt=(
        "You are a helpful critic agent. "
        "Your task is to validate research findings, and remove the false ones. "
        "Only use the provided findings, do not create your own or infer ones "
        "that are not provided. " 
        "You do not carry out research, only validating."
    ),
    output_type=Critic
)

