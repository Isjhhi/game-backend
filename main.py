from fastapi import FASTAPI
app = FASTAPI()

@app.get("/")
def hello():
  return{"halo server farm game is online"}
