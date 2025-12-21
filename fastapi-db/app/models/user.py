from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base_class import Base


class User(Base):
    __tablename__ = "users" # ชื่อตารางในฐานข้อมูล

    # คอลัมน์ต่างๆ ในตาราง users
    # id, email, hashed_password, is_active, first_name, last_name
    # String(255) กำหนดความยาวสูงสุดของสตริง
    # String ไม่ได้กำหนดความยาวสูงสุดจึงใช้สำหรับข้อมูลที่ยาวไม่จำกัด
    id = Column(Integer, primary_key=True, index=True) # รหัสผู้ใช้
    first_name = Column(String(128), nullable=False) # ชื่อจริง
    last_name = Column(String(128), nullable=False) # นามสกุล
    email = Column(String(255), unique=True, index=True, nullable=False) # อีเมล
    hashed_password = Column(String, nullable=False) # รหัสผ่านที่ถูกเข้ารหัส
    is_active = Column(Boolean, default=True) # สถานะผู้ใช้ (เปิดใช้งานหรือไม่)

    # ความสัมพันธ์: 1 User มีหลาย Items
    # back_populates จะชี้ไปที่ตัวแปร 'owner' ในไฟล์ Item
    # cascade="all, delete-orphan" หมายความว่า ถ้า User ถูกลบ Items ที่เกี่ยวข้องจะถูกลบด้วย
    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")
