from .critic_agent import agent as critic_agent
from .research_agent import agent as research_agent
from .summarizer_agent import agent as summarizer_agent

async def run_pipeline(topic: str):
    findings = await research_agent.run(f"Carry out extensive research on: {topic}")
    validated = await critic_agent.run(f"Validate the following findings: {findings}")
    summary = await summarizer_agent.run(f"Create a comprehensive summary for these findings: {validated}")
    return summary.output