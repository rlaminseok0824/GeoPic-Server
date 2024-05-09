from config import config
from nest.core.app import App

app = App(
    description="PyNest service",
    modules=[]
)


@app.on_event("startup")
async def startup():
    await config.create_all()
