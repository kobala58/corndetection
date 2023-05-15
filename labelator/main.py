from fastapi import FastAPI
import random
import os

UNLABELED = "../splited/train/tiles_test/"

app = FastAPI()


def grab_unlabeled_photo():
    # files = os.listdir(UNLABELED)
    rnd = random.choice(os.listdir(UNLABELED)) # terrible performance




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/grab_random")
    
