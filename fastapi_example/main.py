
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/hello")
def hello():
    return 'Hello World!'


@app.get("/hello_json")
def hello_json():
    return {"message": 'Hello World!',
            "value": None}



@app.get("/hello_html")
def hello():
    html = """
    <div align="center">Ahoj</div>
    """

    return HTMLResponse(html)



data = {
    "nastroje": {
        1: "kladivo",
        2: "kleste",
        3: "vrtacka",
    },
    "rostliny": {
        1: "kopriva",
        2: "kaktus",
    }
}


@app.get("/catalogue/{item_type}")
def catalogue(item_type, item_id: int):

    if item_type not in data:
        return "Neni to tam."

    items = data[item_type]

    return items.get(item_id)

    # item_type je path parameter
    # item_id je query parameter





if __name__ == '__main__':
    uvicorn.run(app)
