import fastapi as FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message":"your api is running"}