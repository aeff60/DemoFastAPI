from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/result/{score}")
async def predict_species(score):
    score = int(score)
    if(score >= 50):
        result = "Pass"
    else:    
        result = "No pass"
    return {"your result is": result}

    