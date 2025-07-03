# PyUI - A python module for creating user interfaces.

def text(text: str, color: str = "black", size: int = 12, css: str = "") -> str:
    """
    Generates an HTML element with the specified text, color, size, and optional CSS.
    """
    return f'<div style="color:{color}; font-size:{size}px; {css}">{text}</div>'

def paragraph(text: str, color: str = "black", size: int = 12, css: str = "") -> str:
    """
    Generates an HTML paragraph element with the specified text, color, size, and optional CSS.
    """
    return f'<p style="color:{color}; font-size:{size}px; {css}">{text}</p>'

def button(text: str, color: str = "blue", size: int = 12, css: str = "") -> str:
    """
    Generates an HTML button element with the specified text, color, size, and optional CSS.
    """
    return f'<button style="color:{color}; font-size:{size}px; {css}">{text}</button>'

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
        
def css(design):
    """
    Returns the CSS styles for the specified design.
    
    Args:
        design (str): The design type ('cupertino', 'material', 'microwindow', 'skeleton').
        
    Returns:
        str: The CSS styles as a string.
    """
    design = design.lower()
    if design == 'cupertino':
        return Cupertino.get_css()
    elif design == 'material':
        return Material().get_css()
    elif design == 'microwindow':
        return MicroWindow().get_css()
    elif design == 'skeleton':
        return Skeleton().get_css()
    else:
        raise ValueError("Unknown design type")