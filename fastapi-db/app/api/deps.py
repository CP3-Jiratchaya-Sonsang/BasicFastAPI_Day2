from typing import AsyncGenerator
from app.db.session import SessionLocal

# เปลี่ยนจาก Generator ธรรมดา เป็น AsyncGenerator
async def get_db() -> AsyncGenerator:
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            # SessionLocal จะปิดตัวเองอัตโนมัติเมื่อจบ async with
            # หรือถ้าไม่ได้ใช้ context manager ต้อง await db.close() เอง
            pass