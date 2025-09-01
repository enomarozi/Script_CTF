from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyad import aduser
import pythoncom

app = FastAPI()

class UserRequest(BaseModel):
    username: str

class ChangePasswordRequest(BaseModel):
    username: str
    password: str

@app.get("/enomarozi")
async def testing():
    return "enomarozi"

@app.post("/postdata")
async def postdata(request: UserRequest):
    pythoncom.CoInitialize()
    try:
        user = check_user(request.username)
        user_account_control = user.get_attribute("userAccountControl")[0]
        if user_account_control != 512:
            return {"message": None}
        else:
            return {"message": "Success"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/change-password")
async def change_password(request: ChangePasswordRequest):
    pythoncom.CoInitialize()
    try:
        user = check_user(request.username)
        user.set_password(request.password)
        return {"message": "Success"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def check_user(username: str):
    try:
        user = aduser.ADUser.from_cn(username)
        return user
    except Exception:
        raise ValueError("User tidak ada")
