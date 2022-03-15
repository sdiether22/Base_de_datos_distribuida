from fastapi import FastAPI
from routes.user import user
app = FastAPI()

@app.get('/')
def get_raiz():
    return{"Aqui no hay nada, dirigete a /docs"}

app.include_router(user)    