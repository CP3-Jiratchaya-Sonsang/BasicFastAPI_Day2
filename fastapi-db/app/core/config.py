from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # กำหนด Default ได้เฉพาะข้อมูลที่ไม่ใช่ความลับ
    PROJECT_NAME: str = "My FastAPI Project"
    
    # Pydantic จะบังคับให้ไปหาค่านี้จากไฟล์ .env เท่านั้น ถ้าหาไม่เจอโปรแกรมจะ Error
    DATABASE_URL: str 

    class Config:
        env_file = ".env"
        # env_file_encoding = 'utf-8'

settings = Settings()