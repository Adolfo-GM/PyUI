from pyui_assets import web
from pyui import *

TITLE = "PyUI Example"

APP = contentview(
    heading("Welcome to PyUI!"),
    paragraph("This is a simple example of a PyUI application."),
    button("Click Me", onclick="alert('Button clicked!')"),
    css('material'),
)

web.show_html_window(APP, width=800, height=600, title=TITLE)

