from starlette.applications import Starlette
from starlette.responses import JSONResponse
from mangum import Mangum

app = Starlette()


@app.route("/")
async def homepage(request):
    return JSONResponse({"hello": "world"})


def lambda_handler(event, context):
    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(event, context)
