import webbrowser
import threading
from app import app

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    # Open browser after 1.5 seconds
    threading.Timer(1.5, open_browser).start()
    # Start Flask
    app.run(debug=True, port=5000)