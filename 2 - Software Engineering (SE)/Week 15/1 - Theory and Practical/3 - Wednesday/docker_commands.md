# Common Docker Commands and Their Explanations

Docker simplifies application deployment by packaging applications and their dependencies into containers. Below are some essential Docker commands that you'll frequently use while working with Docker.

## Docker Commands Overview

### 1. Docker Version and System Information

- **`docker -v`** or **`docker --version`**
  ```bash
  docker -v
  ```
  Displays the installed Docker version.

- **`docker info`**
  ```bash
  docker info
  ```
  Provides detailed information about the Docker installation, including the number of containers, images, and system resources.

### 2. Docker Images

- **`docker pull`**
  ```bash
  docker pull <image-name>
  ```
  Downloads a Docker image from a registry (e.g., Docker Hub).

  Example:
  ```bash
  docker pull nginx
  ```
  Pulls the official `nginx` image from Docker Hub.

- **`docker build`**
  ```bash
  docker build -t <image-name> <path-to-dockerfile>
  ```
  Builds a Docker image from a specified `Dockerfile`.

  Example:
  ```bash
  docker build -t my_app .
  ```
  Builds an image named `my_app` from the `Dockerfile` in the current directory.

- **`docker images`**
  ```bash
  docker images
  ```
  Lists all Docker images on the local system.

- **`docker rmi`**
  ```bash
  docker rmi <image-name-or-id>
  ```
  Removes one or more Docker images.

  Example:
  ```bash
  docker rmi my_app
  ```
  Removes the image named `my_app`.

### 3. Docker Containers

- **`docker run`**
  ```bash
  docker run [OPTIONS] <image-name> [COMMAND] [ARG...]
  ```
  Runs a command in a new container from a specified image.

  Example:
  ```bash
  docker run -d -p 80:80 nginx
  ```
  Runs the `nginx` image in detached mode (`-d`) and maps port 80 of the host to port 80 of the container.

- **`docker ps`**
  ```bash
  docker ps
  ```
  Lists all running containers.

  To include stopped containers, use:
  ```bash
  docker ps -a
  ```

- **`docker stop`**
  ```bash
  docker stop <container-id>
  ```
  Stops a running container.

  Example:
  ```bash
  docker stop my_container
  ```
  Stops the container with the name or ID `my_container`.

- **`docker start`**
  ```bash
  docker start <container-id>
  ```
  Starts a stopped container.

  Example:
  ```bash
  docker start my_container
  ```
  Starts the container with the name or ID `my_container`.

- **`docker rm`**
  ```bash
  docker rm <container-id>
  ```
  Removes one or more stopped containers.

  Example:
  ```bash
  docker rm my_container
  ```
  Removes the container with the name or ID `my_container`.

### 4. Docker Volumes

- **`docker volume create`**
  ```bash
  docker volume create <volume-name>
  ```
  Creates a new volume.

  Example:
  ```bash
  docker volume create my_volume
  ```
  Creates a volume named `my_volume`.

- **`docker volume ls`**
  ```bash
  docker volume ls
  ```
  Lists all Docker volumes on the local system.

- **`docker volume rm`**
  ```bash
  docker volume rm <volume-name>
  ```
  Removes a volume.

  Example:
  ```bash
  docker volume rm my_volume
  ```
  Removes the volume named `my_volume`.

### 5. Docker Networks

- **`docker network create`**
  ```bash
  docker network create <network-name>
  ```
  Creates a new network.

  Example:
  ```bash
  docker network create my_network
  ```
  Creates a network named `my_network`.

- **`docker network ls`**
  ```bash
  docker network ls
  ```
  Lists all Docker networks on the local system.

- **`docker network rm`**
  ```bash
  docker network rm <network-name>
  ```
  Removes a network.

  Example:
  ```bash
  docker network rm my_network
  ```
  Removes the network named `my_network`.

### 6. Docker Compose

- **`docker-compose up`**
  ```bash
  docker-compose up
  ```
  Builds, (re)creates, starts, and attaches to containers for a service defined in a `docker-compose.yml` file.

  To run in detached mode, use:
  ```bash
  docker-compose up -d
  ```

- **`docker-compose down`**
  ```bash
  docker-compose down
  ```
  Stops and removes containers, networks, volumes, and images created by `docker-compose up`.

- **`docker-compose build`**
  ```bash
  docker-compose build
  ```
  Builds or rebuilds services defined in a `docker-compose.yml` file.

- **`docker-compose ps`**
  ```bash
  docker-compose ps
  ```
  Lists containers related to the services defined in a `docker-compose.yml` file.

### 7. Inspecting and Debugging

- **`docker logs`**
  ```bash
  docker logs <container-id>
  ```
  Fetches the logs of a container.

  Example:
  ```bash
  docker logs my_container
  ```
  Fetches logs for the container named `my_container`.

- **`docker exec`**
  ```bash
  docker exec -it <container-id> <command>
  ```
  Runs a command in a running container.

  Example:
  ```bash
  docker exec -it my_container /bin/bash
  ```
  Opens an interactive shell in the container named `my_container`.

- **`docker inspect`**
  ```bash
  docker inspect <container-id-or-image-name>
  ```
  Returns detailed information about a container or image.

  Example:
  ```bash
  docker inspect my_container
  ```
  Provides detailed information about the container named `my_container`.

### 8. Cleaning Up

- **`docker system prune`**
  ```bash
  docker system prune
  ```
  Removes unused data, including stopped containers, unused networks, and dangling images.

  To remove all unused images, containers, and volumes, use:
  ```bash
  docker system prune -a
  ```

---