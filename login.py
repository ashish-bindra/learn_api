
from fastapi import FastAPI, Request,Form,Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse,HTMLResponse,JSONResponse

from jose import jwt,JWTError
from datetime import datetime,timedelta

SECRET_KEY = "abcd"
ALGORITHM = "HS256"
fake_users_db = {
    "admin": {"user_email":"abc", "user_password":"123"}
    }

app = FastAPI()

# Dependency to Verify Token
def get_current_user(request: Request):
    token = request.cookies.get("token")  # Token stored in HTTP-only cookie
    if not token:
        # Redirect to login with a message if no token is found
        return RedirectResponse(url="/login?message=Please+log+in", status_code=302)

    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in fake_users_db:
            # Redirect for invalid credentials
            return RedirectResponse(url="/login?message=Invalid+credentials", status_code=302)
    except JWTError:
        # Redirect for an invalid or expired token
        return RedirectResponse(url="/login?message=Session+expired,+please+log+in+again", status_code=302)

    return username

@app.get("/", response_class=JSONResponse)
@app.get("/login", response_class=JSONResponse)
async def main(request: Request, message: str = None):
    """
    API endpoint to return a JSON response with an optional message.
    :param message: Optional message to display (e.g., error messages).
    :param request: The current request object.
    :return: A JSON response with the message.
    """
    response_data = {
        "message": message if message else "Welcome to the login API!",
        "status": "success"
    }
    # return JSONResponse(content=response_data)
    return response_data
# Login Functionality
@app.post("/login")
async def user_login(
        user_email: str = Form(...),
        user_password: str = Form(...),
):
    """
    Handle user login.
    :param request: The current request object.
    :param user_email: The email provided by the user.
    :param user_password: The password provided by the user.
    :return: Redirect to the dashboard if login is successful, else return an error message in JSON.
    """
    # Validate credentials
    user = fake_users_db.get("admin")
    print(user)
    if not user or user["user_email"] != user_email or user["user_password"] != user_password:
        message = "Invalid email or password. Please try again."
        return JSONResponse(content={"message": message}, status_code=401)

    # Generate access token (JWT)
    access_token = jwt.encode(
        {"sub": "admin", "exp": datetime.utcnow() + timedelta(minutes=30)},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    # Redirect to the dashboard and set token as an HttpOnly cookie
    response = RedirectResponse(url="/dashboard", status_code=302)
    response.set_cookie(key="token", value=access_token, httponly=True, max_age=1800)  # max_age is in seconds
    return response

# Protected Dashboard Route
@app.get("/dashboard")
async def dashboard(request: Request, user: str = Depends(get_current_user)):
    """
    Display the dashboard for authenticated users.
    :param request: The current request object.
    :param user: The currently logged-in user (validated by the dependency).
    :return: The dashboard template response.
    """
    # Check if user is actually a RedirectResponse
    if isinstance(user, RedirectResponse):
        return user  # Redirect if not authenticated
    return {"user": user}


# Logout Route
@app.get("/logout")
async def logout():
    """
    Log out the user by deleting the authentication token.
    :return: Redirect to the login page.
    """
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie(key="token")
    return response


