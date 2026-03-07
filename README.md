# QR Code Generator

A CLI-based QR code generator app for social media profiles and custom URLs

## Supported Platforms

| Platform | What you enter |
|----------|---------------|
| LinkedIn | Username (e.g., `yourprofile`) |
| Instagram | Handle (e.g., `yourhandle`) |
| Facebook | Username (e.g., `yourprofile`) |
| GitHub | Username (e.g., `yourusername`) |
| Medium | Handle (e.g., `yourhandle`) |
| X (Twitter) | Handle (e.g., `yourhandle`) |
| YouTube | Channel name (e.g., `yourchannel`) |
| Custom URL | Any full URL |

## Prerequisites

- [Python](https://www.python.org/) 3.8 or higher and pip, **or**
- [Docker](https://www.docker.com/)

## Installation

### Option 1: Python (pip)

```bash
git clone https://github.com/yourusername/QRcodegenerator.git
cd QRcodegenerator
pip install -e .
```

### Option 2: Docker

```bash
git clone https://github.com/yourusername/QRcodegenerator.git
cd QRcodegenerator
docker build -t qrcodegenerator .
```

## Usage

### Python

```bash
qrcodegenerator start                # default port 3001
qrcodegenerator start --port 8080    # custom port
qrcodegenerator start -p 4000        # short alias
qrcodegenerator stop                 # stop the running server
qrcodegenerator --help               # help
```

The app will automatically open in your browser at `http://localhost:3001`.

### Docker

```bash
docker run -p 3001:3001 qrcodegenerator
```

Custom port:

```bash
docker run -p 8080:8080 qrcodegenerator qrcodegenerator start --port 8080
```

Then open `http://localhost:3001` (or your custom port) in your browser.

## How It Works

1. Run the app using one of the commands above
2. Click a platform button (LinkedIn, GitHub, YouTube, etc.)
3. Enter your username — the full URL is built automatically
4. Click **Generate QR** to create your QR code
5. Click **Download PNG** to save it

## Project Structure

```
QRcodegenerator/
├── qrcodegenerator/
│   ├── __init__.py
│   ├── cli.py          # Flask app + CLI entry point
│   └── templates/
│       └── index.html  # App UI
├── pyproject.toml      # Package config + CLI entry point
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Features

- Auto-opens browser on start
- Auto-builds profile URLs from just a username
- Website favicon overlay on QR codes
- Download QR code as PNG with logo
- Works on macOS, Windows, and Linux
- Graceful shutdown with Ctrl+C
- `qrcodegenerator stop` to cleanly stop the server

## Author

Built by [Mahendran Selvakumar](https://github.com/skmahe1077)

## License

MIT
