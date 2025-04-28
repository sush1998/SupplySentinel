import asyncio
from app.agent.background_agent import start_agent_loop

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_agent_loop())
