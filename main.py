from fastapi import FASTAPI
app = FASTAPI()

app.get("/")
def hello():
  print("halo server farm game is online")
