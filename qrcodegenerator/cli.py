#!/usr/bin/env python3

import argparse
import os
import signal
import sys
import webbrowser

import requests
from flask import Flask, render_template, request, Response

PID_FILE = os.path.join(os.path.expanduser("~"), ".qrcodegenerator.pid")

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/favicon-proxy")
def favicon_proxy():
    domain = request.args.get("domain", "")
    sz = request.args.get("sz", "128")
    if not domain:
        return Response(status=400)
    url = f"https://www.google.com/s2/favicons?domain={domain}&sz={sz}"
    try:
        resp = requests.get(url, timeout=5)
        return Response(resp.content, content_type=resp.headers.get("Content-Type", "image/png"))
    except Exception:
        return Response(status=502)


def open_browser(url):
    """Open the default browser cross-platform."""
    try:
        webbrowser.open(url)
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(
        prog="qrcodegenerator",
        description="QR Code Generator - Generate QR codes for social profiles and websites",
    )
    subparsers = parser.add_subparsers(dest="command")

    start_parser = subparsers.add_parser("start", help="Start the QR Code Generator app")
    start_parser.add_argument(
        "--port", "-p", type=int, default=3001, help="Port to run on (default: 3001)"
    )

    subparsers.add_parser("stop", help="Stop the running QR Code Generator app")

    args = parser.parse_args()

    if args.command == "stop":
        stop_server()
    elif args.command == "start":
        start_server(args.port)
    else:
        parser.print_help()
        sys.exit(0)


def start_server(port):
    if port < 1 or port > 65535:
        print(f"\n  Invalid port. Use a number between 1 and 65535.\n")
        sys.exit(1)

    # Save PID for stop command
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))

    url = f"http://localhost:{port}"
    print(f"""
  ╔══════════════════════════════════════╗
  ║       QR Code Generator App         ║
  ╠══════════════════════════════════════╣
  ║                                      ║
  ║   Running at: http://localhost:{str(port):<5s}║
  ║                                      ║
  ║   Press Ctrl+C to stop               ║
  ╚══════════════════════════════════════╝
    """)

    if not os.environ.get("RUNNING_IN_DOCKER"):
        open_browser(url)

    try:
        app.run(host="0.0.0.0", port=port)
    finally:
        cleanup_pid()


def stop_server():
    if not os.path.exists(PID_FILE):
        print("\n  No running server found.\n")
        sys.exit(1)

    with open(PID_FILE) as f:
        pid = int(f.read().strip())

    try:
        os.kill(pid, signal.SIGTERM)
        print(f"\n  Server (PID {pid}) stopped.\n")
    except ProcessLookupError:
        print(f"\n  Server (PID {pid}) is not running.\n")
    finally:
        cleanup_pid()


def cleanup_pid():
    try:
        os.remove(PID_FILE)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
