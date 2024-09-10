from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from similarity import determine_general_similarity
from pydantic import BaseModel

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    new_message: str
    old_messages: list[str]

@app.post("/similarity")
async def root(user_messages: Input):
    new_message = user_messages.new_message
    old_messages = user_messages.old_messages
    return {"similarity": determine_general_similarity(new_message, old_messages)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)