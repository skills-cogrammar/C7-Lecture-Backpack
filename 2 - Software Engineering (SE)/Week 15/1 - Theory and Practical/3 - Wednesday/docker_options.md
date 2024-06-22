# Common Docker Options and Their Explanations

Docker options (or flags) provide additional parameters to customize the behavior of Docker commands. Below are some frequently used options across various Docker commands.

## Docker Options Overview

### General Options

- **`-d` or `--detach`**
  ```bash
  docker run -d <image-name>
  ```
  Runs a container in detached mode (in the background).

  Example:
  ```bash
  docker run -d nginx
  ```
  Runs the `nginx` container in the background.

- **`-it`**
  ```bash
  docker run -it <image-name> /bin/bash
  ```
  Runs a container interactively with a terminal session.

  Example:
  ```bash
  docker run -it ubuntu /bin/bash
  ```
  Starts an interactive bash shell in an `ubuntu` container.

- **`-p` or `--publish`**
  ```bash
  docker run -p <host-port>:<container-port> <image-name>
  ```
  Maps a container’s port to a host port.

  Example:
  ```bash
  docker run -p 8080:80 nginx
  ```
  Maps port 80 in the `nginx` container to port 8080 on the host machine.

- **`--name`**
  ```bash
  docker run --name <container-name> <image-name>
  ```
  Assigns a name to the container.

  Example:
  ```bash
  docker run --name my_nginx -d nginx
  ```
  Runs the `nginx` container in the background with the name `my_nginx`.

- **`-e` or `--env`**
  ```bash
  docker run -e <key>=<value> <image-name>
  ```
  Sets environment variables in the container.

  Example:
  ```bash
  docker run -e "APP_ENV=production" my_app
  ```
  Sets the `APP_ENV` variable to `production` in the `my_app` container.

- **`-v` or `--volume`**
  ```bash
  docker run -v <host-path>:<container-path> <image-name>
  ```
  Mounts a volume by mapping a host directory to a container directory.

  Example:
  ```bash
  docker run -v /my/host/data:/data my_app
  ```
  Maps the host directory `/my/host/data` to the container directory `/data`.

- **`--rm`**
  ```bash
  docker run --rm <image-name>
  ```
  Automatically removes the container when it exits.

  Example:
  ```bash
  docker run --rm my_temp_container
  ```
  Removes `my_temp_container` once it stops running.

### Build Options

- **`-t` or `--tag`**
  ```bash
  docker build -t <image-name> <path-to-dockerfile>
  ```
  Tags the built image with a specified name.

  Example:
  ```bash
  docker build -t my_app:latest .
  ```
  Builds the image and tags it as `my_app:latest`.

- **`-f` or `--file`**
  ```bash
  docker build -f <dockerfile-path> <context-path>
  ```
  Specifies a custom `Dockerfile` for the build.

  Example:
  ```bash
  docker build -f ./Dockerfile.custom -t custom_app .
  ```
  Uses `Dockerfile.custom` to build the `custom_app` image.

- **`--no-cache`**
  ```bash
  docker build --no-cache -t <image-name> <path-to-dockerfile>
  ```
  Builds the image without using the cache.

  Example:
  ```bash
  docker build --no-cache -t fresh_build .
  ```
  Forces a clean build of the image `fresh_build` without cached layers.

### Container Management Options

- **`-a` or `--all`**
  ```bash
  docker ps -a
  ```
  Lists all containers, including those that are stopped.

- **`--filter`**
  ```bash
  docker ps --filter "status=exited"
  ```
  Filters containers based on a specified condition.

  Example:
  ```bash
  docker ps --filter "name=my_app"
  ```
  Lists containers with names matching `my_app`.

- **`-q` or `--quiet`**
  ```bash
  docker ps -q
  ```
  Outputs only the container IDs.

  Example:
  ```bash
  docker ps -q --filter "status=exited"
  ```
  Lists only the IDs of exited containers.

- **`-f` or `--force`**
  ```bash
  docker rm -f <container-id>
  ```
  Forces the removal of a running container.

  Example:
  ```bash
  docker rm -f my_app
  ```
  Forcefully stops and removes the container named `my_app`.

- **`--volume`**
  ```bash
  docker rm --volume <container-id>
  ```
  Removes the associated volumes when removing a container.

  Example:
  ```bash
  docker rm --volume my_app
  ```
  Removes the container `my_app` along with its volumes.

### Docker Compose Options

- **`-d` or `--detach`**
  ```bash
  docker-compose up -d
  ```
  Runs Docker Compose services in the background.

- **`--build`**
  ```bash
  docker-compose up --build
  ```
  Builds the images before starting the services.

- **`--scale`**
  ```bash
  docker-compose up --scale <service>=<number>
  ```
  Scales the specified service to the given number of instances.

  Example:
  ```bash
  docker-compose up --scale web=3
  ```
  Runs 3 instances of the `web` service.

- **`-f` or `--file`**
  ```bash
  docker-compose -f <compose-file> up
  ```
  Specifies an alternate `docker-compose.yml` file.

  Example:
  ```bash
  docker-compose -f docker-compose.prod.yml up
  ```
  Uses `docker-compose.prod.yml` for the Compose configuration.

### Network Options

- **`-d` or `--driver`**
  ```bash
  docker network create -d <driver-name> <network-name>
  ```
  Specifies the network driver to use when creating a network.

  Example:
  ```bash
  docker network create -d bridge my_bridge_network
  ```
  Creates a network named `my_bridge_network` using the `bridge` driver.

- **`--subnet`**
  ```bash
  docker network create --subnet=<subnet> <network-name>
  ```
  Specifies a custom subnet for the network.

  Example:
  ```bash
  docker network create --subnet=192.168.1.0/24 my_custom_network
  ```
  Creates a network `my_custom_network` with the subnet `192.168.1.0/24`.

### Logging and Debugging Options

- **`-f` or `--follow`**
  ```bash
  docker logs -f <container-id>
  ```
  Continuously streams logs from a container.

- **`--tail`**
  ```bash
  docker logs --tail <number-of-lines> <container-id>
  ```
  Shows the specified number of log lines from the end.

  Example:
  ```bash
  docker logs --tail 10 my_container
  ```
  Displays the last 10 lines of logs from `my_container`.

- **`-t` or `--timestamps`**
  ```bash
  docker logs -t <container-id>
  ```
  Shows timestamps for each log entry.

### Resource Management Options

- **`--memory`**
  ```bash
  docker run --memory <memory-limit> <image-name>
  ```
  Limits the memory usage of a container.

  Example:
  ```bash
  docker run --memory 256m my_app
  ```
  Restricts the `my_app` container to use at most 256 MB of memory.

- **`--cpus`**
  ```bash
  docker run --cpus <number-of-cpus> <image-name>
  ```
  Limits the number of CPUs available to a container.

  Example:
  ```bash
  docker run --cpus 1.5 my_app
  ```
  Allocates 1.5 CPUs to the `my_app` container.

- **`--restart`**
  ```bash
  docker run --restart <policy> <image-name>
  ```
  Configures the restart policy for a container.

  Example:
  ```bash
  docker run --restart always my_app
  ```
  Ensures that `my_app` restarts automatically if it stops.

---
