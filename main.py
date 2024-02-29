# notes:

# run the following
# pip install fastapi
# pip install uvicorn[standard]
# docs for the api routes are on "localhost:8000/docs" and localhost:8000/redocs"
# check both, they essentially tell the same story, but one explains what the route does and the other allows you to check the route
# also, default port is 8000.....kinda obvious but stating 😂😂😂


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}