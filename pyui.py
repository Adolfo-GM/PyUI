# PyUI - A python module for creating user interfaces.

def text(text: str, color: str = "black", size: int = 12, css: str = "") -> str:
    """
    Generates an HTML element with the specified text, color, size, and optional CSS.
    """
    return f'<div style="color:{color}; font-size:{size}px; {css}">{text}</div>'

def heading(text: str, level: int = 1, color: str = "black", size: int = 12, css: str = "") -> str:
    """
    Generates an HTML heading element with the specified text, level, color, size, and optional CSS.
    
    Args:
        text (str): The text to display in the heading.
        level (int): The heading level (1-6).
        color (str): The color of the text.
        size (int): The font size in pixels.
        css (str): Additional CSS styles as a string.
    
    Returns:
        str: An HTML string representing the heading element.
    """
    if level < 1 or level > 6:
        raise ValueError("Heading level must be between 1 and 6.")
    return f'<h{level} style="color:{color}; font-size:{size}px; {css}">{text}</h{level}>'

def paragraph(text: str, color: str = "black", size: int = 12, css: str = "") -> str:
    """
    Generates an HTML paragraph element with the specified text, color, size, and optional CSS.
    """
    return f'<p style="color:{color}; font-size:{size}px; {css}">{text}</p>'

def button(text: str, color: str = "blue", size: int = 12, css: str = "", onclick: str = "") -> str:
    """
    Generates an HTML button element with the specified text, color, size, and optional CSS.
    """
    return f'<button style="color:{color}; font-size:{size}px; {css}" onclick="{onclick}">{text}</button>'

def javascript(code: str) -> str:
    """
    Generates a script tag with the provided JavaScript code.
    """
    return f'<script>{code}</script>'

def script(src: str) -> str:
    """
    Generates a script tag with the provided source URL.
    """
    return f'<script src="{src}"></script>'

def link(rel: str, href: str) -> str:
    """
    Generates a link tag for stylesheets or other resources.
    """
    return f'<a href="{href}" rel="{rel}"></a>'

class Element:
    def __init__(self, tag, content, style=""):
        self.tag = tag
        self.content = content
        self.style = style

    def render(self):
        return f'<{self.tag} style="{self.style}">{self.content}</{self.tag}>'

class Cupertino:
    """
    A class to represent a Cupertino-style UI component.
    """
    def get_css(self):
        """
        Returns the CSS styles for Cupertino components.
        """
        file = 'pyui_assets/cupertino.css'
        with open(file, 'r') as f:
            return f.read()
        
class Material:
    """
    A class to represent a Material-style UI component.
    """
    def get_css(self):
        """
        Returns the CSS styles for Material components.
        """
        file = 'pyui_assets/material.css'
        with open(file, 'r') as f:
            return f.read()

class MicroWindow:
    """
    A class to represent a MicroWindow-style UI component.
    """
    def get_css(self):
        """
        Returns the CSS styles for MicroWindow components.
        """
        file = 'pyui_assets/microwindow.css'
        with open(file, 'r') as f:
            return f.read()
    
class Skeleton:
    """
    A class to represent a Skeleton-style UI component.
    """
    def get_css(self):
        """
        Returns the CSS styles for Skeleton components.
        """
        file = 'pyui_assets/skeleton.css'
        with open(file, 'r') as f:
            return f.read()

def style_tag(func):
    def wrapper(*args, **kwargs):
        css_code = func(*args, **kwargs)
        return f"<style>{css_code}</style>"
    return wrapper
  
@style_tag
def css(design):
    """
    Returns the CSS code for the specified design type.
    """
    design = design.lower().strip()
    if design == 'cupertino':
        return Cupertino().get_css()
    elif design == 'material':
        return Material().get_css()
    elif design == 'microwindow':
        return MicroWindow().get_css()
    elif design == 'skeleton':
        return Skeleton().get_css()
    else:
        raise ValueError("Unknown design type")

def contentview(*elements, title="PyUI App") -> str:
    """
    Generates a full HTML document from the given UI elements.

    Args:
        *elements: UI element strings (from text(), button(), etc.)
        title (str): The title of the HTML document.
        css_code (str): Optional CSS code to include in a <style> tag.

    Returns:
        str: Complete HTML document as a string.
    """
    body_content = "\n".join(elements)
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
{body_content}
</body>
</html>
"""
