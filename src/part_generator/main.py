from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import datetime

from part_generator.api.schemas import WasherRequest, BoltRequest
from part_generator.services.gen_fastener import generate_washer, generate_bolt, export_result

app = FastAPI()

# for UI template
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# UI endpoint
@app.get("/")
def home_root(request: Request, part: str = "washer"):
    return templates.TemplateResponse(request=request, name="gui_template.html", context={"part": part})

# Washer generation endpoint - accepts POST request with JSON body containing outer_diameter, inner_diameter, thickness
@app.post("/v1/generate/washer")
def washer_request(request: WasherRequest):

    try: 
        result = generate_washer(request.outer_diameter, request.inner_diameter, request.thickness)
        filename = f'washer_temp_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.step'
        export_result(result, filename)

        return FileResponse(
                path=filename,
                filename=filename,
                media_type="application/octet-stream",
            )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Bolt generation endpoint - accepts POST request with JSON body containing diameter, length
@app.post("/v1/generate/bolt")
def bolt_request(request: BoltRequest):
    try:
        result = generate_bolt(request.diameter, request.length)
        filename = f'bolt_temp_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.step'
        export_result(result, filename)

        return FileResponse(
                path=filename,
                filename=filename,
                media_type="application/octet-stream",
            )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))