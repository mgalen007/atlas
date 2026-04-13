from .config.models import google_model
from pydantic import BaseModel, Field
from pydantic_ai import Agent

# Output format
class Summary(BaseModel):
    topic: str = Field(
        description="The topic of the research summary."
    )
    key_findings: list[str] = Field(
        description="These are the key findings from the research."
    )
    content: str = Field(
        description="This is the content of the summary, including the valid findings."
    )

# The summarizer agent
agent = Agent(
    name="Summarizer Agent",
    model=google_model,
    system_prompt=(
        "You are helpful summarizer agent. "
        "Your task is to take the provided research findings, and provide an excellent summary. "
        "Only use the findings provided, do not include the false / invalidated ones. "
        "You only create summaries, no research, no validation."
    ),
    output_type=Summary
)