```markdown
# 🧠 Online CV + AI Chatbot

A Flask-based web app that hosts my **online CV** and includes an **AI chatbot**.  
This project demonstrates **containerization with Docker** and **local Kubernetes deployment (Minikube)** — a full DevOps showcase.

---

## 🏗 Project Structure

```

📂 online-cv-chatbot/
├── app.py
├── requirements.txt
├── Dockerfile
├── k8s-deployment.yaml
├── README.md
└── .gitignore

````

---

## 🐳 Docker Setup

Build and run the Docker container locally:

```bash
# Build the Docker image
docker build -t online-cv-with-chatbot:latest .

# Run the container locally
docker run -p 5000:5000 online-cv-with-chatbot:latest
````

Access the app in your browser:
[http://localhost:5000](http://localhost:5000)

---

## ☸️ Kubernetes Deployment (Minikube)

Deploy the app in a local Kubernetes cluster:

```bash
# Start Minikube (Docker driver)
minikube start --driver=docker

# Load the local Docker image into Minikube
minikube image load online-cv-with-chatbot:latest

# Apply the Deployment and Service YAML
kubectl apply -f k8s-deployment.yaml

# Open the app in your browser
minikube service online-cv-chatbot-service
```

Access URL example: [http://localhost:30000](http://localhost:30000)

---

## 🔧 Tech Stack

* **Python / Flask** – backend web framework
* **Docker** – containerization for consistent environments
* **Kubernetes (Minikube)** – orchestration for local cluster deployment
* **VS Code** – development environment
* **GitHub** – version control and portfolio showcase

---

## 🏅 Skills Demonstrated

* Containerizing a Flask web app with Docker
* Running and exposing Docker containers locally
* Deploying a containerized app to a Kubernetes cluster
* Writing Deployment and Service manifests (YAML)
* Managing local Kubernetes cluster with Minikube
* Using Git and GitHub to track code and infrastructure

---

## 📸 Demo / Screenshots

```markdown
![App Screenshot](images/app-preview.png)
```