# นำเข้า FastAPI จากไลบรารี fastapi
from fastapi import FastAPI

# สำหรับ Scalar API reference
from scalar_fastapi import get_scalar_api_reference

# สร้างแอปพลิเคชัน FastAPI
app = FastAPI()


# สร้างเส้นทาง (route) สำหรับ root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI with uv!"}


# เส้นทาง API สำหรับดู Scalar API reference
# Path: /scalar
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        # title="Scalar FastAPI API Reference",
        title=app.title,
    )