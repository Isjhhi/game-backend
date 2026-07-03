from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
  return{"halo server farm game is online"}
