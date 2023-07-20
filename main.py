from src.app import Application
from src.repository import Content

if __name__ == "__main__":
    content = Content()
    app = Application(content)
    app.run()
