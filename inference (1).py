# inference.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/OpenEnv/Reset")
def openenv_reset():
    # This must return exactly what OpenEnv expects
    return JSONResponse(content={
        "output_box": "",
        "graph": None,
        "score_box": 0.0,
        "task_dropdown": "Echo Task",
        "steps_input": 3
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
