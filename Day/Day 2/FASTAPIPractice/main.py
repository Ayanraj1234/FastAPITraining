from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World","number":44,"is_fun":True}
def avneesh():
    return {"bkl randi kutte ka baccha"}