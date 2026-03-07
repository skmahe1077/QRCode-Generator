#!/usr/bin/env python3

import argparse
import os
import sys
import webbrowser

from flask import Flask, render_template

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/")
def index():
    return render_template("index.html")


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

    args = parser.parse_args()

    if args.command != "start":
        parser.print_help()
        sys.exit(0)

    port = args.port
    if port < 1 or port > 65535:
        print(f"\n  Invalid port. Use a number between 1 and 65535.\n")
        sys.exit(1)

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
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
