from fastapi import APIRouter, HTTPException
from ..agents.service import run_pipeline
from ..agents.summarizer_agent import Summary

# Router instance
router = APIRouter(tags=["Research router"])

# Single endpoint
@router.get("")
async def do_research(topic: str):
    print("Request reached endpoint: /api/research")
    try: 
        summary: Summary = await run_pipeline(topic)
        result = summary.model_dump()
        return {
            "success": True,
            "data": result
        }
    except Exception as e: 
        print(f"Error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Couldn't finish research, try again later."
        )




