from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.route import router

app = FastAPI()

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins, "*" allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # List of allowed methods, "*" allows all methods
    allow_headers=["*"],  # List of allowed headers, "*" allows all headers
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
