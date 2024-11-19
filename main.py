import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    host_ip = request.client.host
    return {"Your IP": host_ip}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)