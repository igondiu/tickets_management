import socket
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    tags=["service_info"],
    responses={
        404: {"description": "Route doesn't exist"}
    }
)


@router.get("/")
def welcome_page():
    """Simple HTML page that helps to rapidly retrieve the link to the API documentation or to the information page"""
    html_code = """
    <!DOCTYPE html>
    <html>
    <body>
    <h1>Tickets manager welcome page</h1>
    <ul>
      <li><a href="/docs">SWAGGER</a></li>
      <li><a href="/locate">LOCATE</a></li>
    </ul>
    </body>
    </html> """
    return HTMLResponse(html_code)


@router.get("/locate")
def locate_route():
    """Provides useful information about the host where the app is running."""
    hostname = socket.gethostname()
    # ip_addr = socket.gethostbyname(hostname)

    return {"hostname": hostname, "ip_addr": ""}
