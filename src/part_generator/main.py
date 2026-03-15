from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from part_generator.api.schemas import WasherRequest, BoltRequest
from part_generator.services.gen_fastener import generate_washer, generate_bolt, export_result

app = FastAPI()

@app.post("/v1/generate/washer")
def washer_request(request: WasherRequest):

    try: 
        result = generate_washer(request.outer_diameter, request.inner_diameter, request.thickness)
        filename = 'washer_temp.step'
        export_result(result, filename)

        return FileResponse(
                path=filename,
                filename="washer.step",
                media_type="application/octet-stream",
            )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/v1/generate/bolt")
def bolt_request(request: BoltRequest):
    try:
        result = generate_bolt(request.diameter, request.length)
        filename = 'bolt_temp.step'
        export_result(result, filename)

        return FileResponse(
                path=filename,
                filename="bolt.step",
                media_type="application/octet-stream",
            )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))