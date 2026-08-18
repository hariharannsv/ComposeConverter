# ComposeConverter

A Flask-based web application that converts Docker Compose YAML files into Kubernetes YAML manifests using Kompose.

## Features

- Upload a Docker Compose `.yml` or `.yaml` file
- Validate the uploaded file type
- Convert Docker Compose configuration using Kompose
- Generate a Kubernetes YAML file
- Download the generated Kubernetes configuration
- Simple Bootstrap-based web interface

## Tech Stack

- Python
- Flask
- Werkzeug
- Kompose
- Docker / Kubernetes
- Bootstrap 5

## Project Structure

```text
ComposeConverter/
├── app/
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   ├── uploads/
│   └── generated/
├── ComposeConverter.ipynb
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ComposeConverter.git
cd ComposeConverter
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Kompose

Install Kompose and make sure the `kompose` command is available in your system PATH.

Check:

```bash
kompose version
```

### 5. Start the application

```bash
python app/main.py
```

Open:

```text
http://127.0.0.1:5000
```

Upload a Docker Compose YAML file and download the generated Kubernetes YAML.

## Docker

Build and run:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:5000
```

## Example

Input Docker Compose:

```yaml
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

The application passes the file to Kompose and produces Kubernetes resources such as a Deployment and Service.

## Project Notebook

`ComposeConverter.ipynb` contains the development and testing workflow used to build the application, including Flask setup, Kompose testing, sample Docker Compose conversion, and Flask server execution.

## Author

Hariharann S V

---

This project is intended for learning and demonstration of Docker Compose to Kubernetes conversion using Flask and Kompose.
