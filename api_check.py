from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/version")
def get_version():
    return {"version": "1.0.0"}

@app.post("/check_prime")
async def check_prime(request: Request):
    data = await request.json() 
    value = data.get("value")    

    if not isinstance(value, int):
        return {"error": "Value must be an integer"}

    if value < 2:
        return {"is_prime": False}

    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

if __name__ == "__main__":
    uvicorn.run("api_check:app", host="0.0.0.0", port=8001, reload=True)