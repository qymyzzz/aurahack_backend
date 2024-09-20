from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.generate_presentation import router as generate_presentaiton

app = FastAPI()

origins = [
    "http://localhost:3000",
    "aurahack.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(generate_presentaiton)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)

# python -m uvicorn main:app --reload
