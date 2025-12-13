from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI"}

@app.get("/joke")
def Joke():
    return {"author": "Sergei",
            "joke": "FKFKKFKFKFKF"}

@app.get("/telegram")
def tg():
    return {"Telegram": "@Forverunu"}

@app.get("/what")
def what():
    return {"message": "what?"}

@app.get("/haha")
def index():
    return {"jokerge": "hehehe"}
