from fastapi import FastAPI

app = FastAPI(title="BookShelf-EPR API")

@app.get("/")
def root():
    return {"message": "BookShelf-EPR Backend Running!"}

