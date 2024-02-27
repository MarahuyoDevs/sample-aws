from starlette.applications import Starlette
from starlette.responses import JSONResponse
from mangum import Mangum

app = Starlette()


async def homepage(request):
    return JSONResponse({"hello": "world"})


app.add_route("/", homepage, methods=["GET"])

handler = Mangum(app, lifespan="off")
