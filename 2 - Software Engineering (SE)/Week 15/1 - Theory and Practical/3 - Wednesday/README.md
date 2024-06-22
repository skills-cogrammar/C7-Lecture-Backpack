# Docker Guide: Running a Python Flask Application

## Part 1: Setting Up Python and Virtual Environments

### Step 1: Clone the Repository
First, clone your repository from GitHub and get into the simple_docker repository:
```bash
git clone https://github.com/yourusername/simple_docker.git
cd simple_docker
```

### Step 2: Set Up a Virtual Environment
A virtual environment is a best practice for managing dependencies in Python projects. It ensures that each project uses only the libraries it needs, avoiding conflicts with other projects.

#### For Windows:
1. Open Command Prompt or PowerShell.
2. Navigate to your project directory.
3. Create a virtual environment:
   ```bash
   python -m venv flask_venv
   ```
4. Activate the virtual environment:
   ```bash
   .\flask_venv\Scripts\activate
   ```
   You should see `(flask_venv)` in your command prompt indicating the virtual environment is active.

#### For macOS and Linux:
1. Open Terminal.
2. Navigate to your project directory.
3. Create a virtual environment:
   ```bash
   python3 -m venv flask_venv
   ```
4. Activate the virtual environment:
   ```bash
   source flask_venv/bin/activate
   ```
   You should see `(flask_venv)` in your terminal indicating the virtual environment is active.

### Step 3: Install Dependencies
Once the virtual environment is activated, install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Server
Start the Flask server using:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000` to see your running Flask application.

---

## Part 2: Installing Docker

Docker simplifies application deployment by packaging an application and its dependencies into a container.

### Step 1: Download and Install Docker
1. Go to the [Docker Desktop download page](https://docs.docker.com/desktop/).
2. Choose the appropriate installer for your operating system (Windows, macOS, or Linux).
3. Follow the prompts to install Docker.

   - **Windows**: Run the Docker Desktop Installer.exe and follow the installation instructions.
   - **macOS**: Open the downloaded `.dmg` file and drag Docker to your Applications folder. Double-click Docker to start the installation.
   - **Linux**: Follow the instructions for your specific distribution on the Docker website.

### Step 2: Verify Docker Installation
After installation, verify that Docker is installed and running by opening a terminal or command prompt and running:
```bash
docker -v
```
You should see the Docker version information if the installation was successful.

---

## Part 3: Building and Running the Docker Container

### Step 0.1: Docker Commands
Please follow this link [Docker Commands](docker_commands.md)

### Step 0.2: Docker Options
Please follow this link [Docker Options](docker_options.md)

### Step 1: Inspect the Dockerfile
The `Dockerfile` in your project directory defines how your Docker image will be built. It typically includes instructions like the base image to use, the dependencies to install, and how to start the application.

### Step 2: Build the Docker Image
Build the Docker image using the following command:
```bash
docker build -t python_flask .
```
The `-t python_flask` tags the image with the name `python_flask`.

### Step 3: Verify the Docker Image
List the Docker images to confirm that your image has been created:
```bash
docker images
```
You should see `python_flask` listed among the images.

### Step 4: Run the Docker Container
Run the container with:
```bash
docker run --name python_flask_test -p 5000:5000 python_flask
```
This command starts the container and maps port 5000 on your host to port 5000 in the container.

### Step 5: Access the Flask Application
Open your web browser and go to `http://127.0.0.1:5000` to see your Flask application running in Docker.

---

### Troubleshooting
- **Virtual Environment Not Activating**: Make sure you are in the correct directory and using the appropriate command for your operating system.
- **Docker Installation Issues**: Ensure your system meets Docker's requirements and that virtualization is enabled in your BIOS/UEFI settings if you're on Windows.
- **Port Conflicts**: If you get an error that port 5000 is already in use, you can change the port mapping in the `docker run` command to use a different host port (e.g., `-p 8080:5000`).

This guide should help you get your Python Flask application up and running with Docker. Happy coding!

---