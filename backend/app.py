from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from functools import lru_cache
from auth import get_current_user
from models import Order, async_session, select, init_db
import asyncio

app = FastAPI(title="Orders API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderIn(BaseModel):
    item: str
    qty: int

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/health")
async def health():
    return {"ok": True}

@app.post("/orders", response_model=OrderIn, status_code=201)
async def create_order(payload: OrderIn, user=Depends(get_current_user)):
    async with async_session() as session:
        session.add(Order(item=payload.item, qty=payload.qty, user_id=user["sub"]))
        await session.commit()
    return payload

@app.get("/orders", response_model=List[OrderIn])
async def list_orders(user=Depends(get_current_user)):
    await asyncio.sleep(0.01)
    async with async_session() as session:
        result = await session.execute(select(Order).where(Order.user_id == user["sub"]))
        rows = result.scalars().all()
    return [OrderIn(item=o.item, qty=o.qty) for o in rows]

@lru_cache(maxsize=32)
def get_allowed_items():
    return {"book", "pen", "notebook"}
