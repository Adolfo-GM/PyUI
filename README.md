<img src="pyui_assets/UI.png" alt="PyUI Logo" width="200">

# PyUI 

PyUI is a python module created by Adolfo GM to create user interfaces.

## Example Code

```python

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

```

<img src="app.png" alt="PyUI Example" width="800">