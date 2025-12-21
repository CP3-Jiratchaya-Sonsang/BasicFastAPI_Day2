from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate

# สมมติว่ามีฟังก์ชัน hash password ใน core/security.py
# from app.core.security import get_password_hash


# ฟังก์ชัน CRUD เกี่ยวกับ User
# ฟังก์ชันดึงข้อมูลผู้ใช้ตาม ID
async def get_user(db: AsyncSession, user_id: int):
    # ใช้ select() แทน query()
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()


# ฟังก์ชันดึงข้อมูลผู้ใช้ตาม email
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()


# ฟังก์ชันดึงรายชื่อผู้ใช้ทั้งหมด (มีการข้ามและจำกัดจำนวน)
async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


# ฟังก์ชันสร้างผู้ใช้ใหม่
async def create_user(db: AsyncSession, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email, 
        hashed_password=fake_hashed_password, 
        first_name=user.first_name,
        last_name=user.last_name
    )
    db.add(db_user)
    await db.commit()  # ต้อง await ตอน commit
    await db.refresh(db_user)  # ต้อง await ตอน refresh
    return db_user
# เพิ่มฟังก์ชันอื่นๆ ตามต้องการ (update, delete)