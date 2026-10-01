from threading import Thread

import webview
from werkzeug.serving import make_server

from app import app


def main():
    server = make_server("127.0.0.1", 0, app, threaded=True)
    server_thread = Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    webview.create_window(
        "Spark",
        f"http://127.0.0.1:{server.server_port}",
        width=1180,
        height=820,
        min_size=(800, 600),
    )
    try:
        webview.start()
    finally:
        server.shutdown()
        server_thread.join()


if __name__ == "__main__":
    main()