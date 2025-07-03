from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
import sys
import os

def show_html_window(html_code: str, width: int = 800, height: int = 600, title: str = "HTML Viewer", icon_path: str = "UI.png"):
    app = QApplication(sys.argv)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_full_path = os.path.join(base_dir, icon_path)
    
    if os.path.exists(icon_full_path):
        icon = QIcon(icon_full_path)
        app.setWindowIcon(icon)
    else:
        print(f"Warning: Icon file not found at {icon_full_path}, no icon will be set.")
        icon = None
    
    window = QMainWindow()
    window.setWindowTitle(title)
    window.resize(width, height)
    if icon:
        window.setWindowIcon(icon)
    
    view = QWebEngineView()
    view.setHtml(html_code)
    window.setCentralWidget(view)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Page</title>
        <style>
            body { background-color: #222; color: #eee; font-family: Arial; }
            h1 { color: #4CAF50; }
        </style>
        <script>
            function showAlert() {
                alert('Hello from JavaScript!');
            }
        </script>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <button onclick="showAlert()">Click Me</button>
    </body>
    </html>
    """
    show_html_window(html_content, width=1000, height=800, title="My Custom HTML Window")
