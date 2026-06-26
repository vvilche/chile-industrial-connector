import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import pytest

class ProjectRootHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serve from the parent directory of this test folder (the project root)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        super().__init__(*args, directory=project_root, **kwargs)

    # Disable standard logging to keep test output clean
    def log_message(self, format, *args):
        pass

@pytest.fixture(scope="session")
def server_url():
    # Bind to localhost on an ephemeral port (0 tells OS to choose free port)
    server = HTTPServer(("127.0.0.1", 0), ProjectRootHTTPRequestHandler)
    host, port = server.server_address
    url = f"http://127.0.0.1:{port}"
    
    # Start server in a background thread
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    
    yield url
    
    # Clean up and shutdown server
    server.shutdown()
    server.server_close()
