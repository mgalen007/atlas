from .config.models import google_model
from pydantic_ai import Agent
from pydantic import BaseModel, Field

# Output format
class Research(BaseModel):
    findings: list[str] = Field(
        description="This is a list of findings on the given topic."
    )

# The research agent
agent = Agent(
    name="Research Agent",
    model=google_model,
    system_prompt=(
        "You are a research agent. "
        "You will be given a topic, and you will make extensive research on it. "
        "Do not speak about things irrelevant to the topic."
    ),
    output_type=Research
)
