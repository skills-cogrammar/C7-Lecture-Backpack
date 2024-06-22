# Multi-Container Docker Application with Flask and MySQL

This repository demonstrates how to use Docker Compose to manage a multi-container application. It includes a simple Flask web application that connects to a MySQL database.

## Project Structure

```
multi-container-app/
│
├── app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│
├── db/
│   └── init.sql
│
└── docker-compose.yml
```

### Description

- **app/**: Contains the Flask application.
  - **app.py**: The main Flask application file.
  - **Dockerfile**: Defines the Docker image for the Flask application.
  - **requirements.txt**: Lists the Python dependencies.

- **db/**: Contains the initial SQL script for setting up the MySQL database.
  - **init.sql**: SQL script to initialize the database and table with sample data.

- **docker-compose.yml**: Defines the services (Flask and MySQL) and their configurations.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
- [DBeaver](https://dbeaver.io/download/) (or any MySQL client) installed if you want to access the database directly.

## Setup and Run

Follow these steps to build and run the application:

### Step 1: Clone the Repository

If you have a specific repository, clone it to your local machine using:

```bash
git clone https://github.com/yourusername/multi-container-app.git
cd multi-container-app
```

otherwise, just use the code provide in the class' repo.

### Step 2: Build and Start the Containers

In the root directory (`multi-container-app/`), use Docker Compose to build and start the containers:

```bash
docker-compose up --build
```

- **`--build`**: Forces a rebuild of the Docker images before starting the containers.
- Docker Compose will:
  - Build the Flask application image.
  - Pull the MySQL image from Docker Hub.
  - Start both containers and set up the MySQL database using the `init.sql` script.

#### MySQL Service Configuration with Docker Compose

This describes the configuration snippet for a Docker service running a MySQL database using Docker Compose.

**Service Definition:**

The service is defined with the following properties:

* **Name:** `db` (This is the name used to refer to the service within the `docker-compose.yml` file)
* **Image:** `mysql:8.0` (This specifies the official MySQL image, version 8.0)
* **Environment:** (Optional) This section defines environment variables accessible within the container.
    * `MYSQL_ROOT_PASSWORD: yy` (Sets the MySQL root user password. **Warning:** Consider a more secure method for storing credentials!)
* **Volumes:** (Optional) This section defines persistent data volumes for the container.
    * `./db/init.sql:/docker-entrypoint-initdb.d/init.sql` (Maps a local directory with an initialization script (`init.sql`) to a location inside the container. This script will be executed when the MySQL server starts.)
* **Ports:** This section maps ports between the container and the host machine.
    * `"3306:3306"` (Maps the container's port 3306 (default MySQL port) to port 3306 on the host machine. This allows connecting to the MySQL server from the host using `localhost:3306` with a MySQL client tool.)

**Explanation:**

This configuration creates a service named "db" that runs a MySQL server (version 8.0) container. The container uses the specified image and optionally sets the root password and mounts a local initialization script. Finally, the port mapping allows connecting to the MySQL server from the host machine.


### Step 3: Access the Application

Once the containers are up and running, you can access the Flask application:

- Open your web browser and go to `http://localhost:5000` to see the Flask app's home page.
- Navigate to `http://localhost:5000/data` to fetch and display data from the MySQL database.

### Step 4: Stop the Containers

To stop and remove the running containers, use:

```bash
docker-compose down
```

This command will stop the containers and remove the associated networks, but it will not remove the built images or the volumes.

## Database Access with DBeaver

You can access the MySQL database using an external application like DBeaver to explore the data directly. Follow these steps:

### Step 1: Install DBeaver

If you haven't installed DBeaver yet, you can download and install it from [DBeaver's official website](https://dbeaver.io/download/).

### Step 2: Configure DBeaver to Connect to MySQL

1. **Open DBeaver**.
2. **Create a new connection** by clicking the `New Database Connection` button.
3. **Select MySQL** from the list of database types.
4. **Enter the connection details**:
   - **Host**: `localhost`
   - **Port**: `3306`
   - **Database**: `docker_practical`
   - **Username**: `root`
   - **Password**: `you_cant_crack_this`
   
   ![DBeaver MySQL Connection](https://www.dbasolved.com/wp-content/uploads/2022/05/image.png)

5. **Test the connection** to ensure that DBeaver can connect to the MySQL server.
6. **Finish** the configuration and connect to the database.

There is a summary in image in this folder images_dbeaver.

### Step 3: Explore the Database

Once connected, you can explore the database:
- View the tables in `docker_practical`.
- Execute SQL queries.
- Browse the data in `regular_customers`.

### Environment Variables

Environment variables are used to configure the MySQL database:
- **MYSQL_ROOT_PASSWORD**: Set to `you_cant_crack_this`.

### Volumes

The MySQL service uses a volume to initialize the database with the `init.sql` script located in the `db/` directory. This script sets up the database and inserts sample data.

## Troubleshooting

- **Logs**: Check the logs for each service using `docker-compose logs`.
- **Rebuild Images**: If you encounter issues, try rebuilding the images using `docker-compose up --build`.
- **Database Connection**: Ensure the Flask application can connect to the MySQL database. The MySQL service should be referred to as `db` (the service name) in the Flask application.

## Learn More

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [DBeaver Documentation](https://dbeaver.io/docs/)

### Additional Information

- The `docker-compose.yml` file has already exposed port `3306` for the MySQL service. This allows external applications to connect to the MySQL server running inside the Docker container.
- Ensure that DBeaver (or any other MySQL client) is installed on your machine. The provided steps for DBeaver can be similarly applied to other MySQL clients.
- The username and password specified (`root` and `you_cant_crack_this`) are from the environment variables configured in the `docker-compose.yml` file.

By following these instructions, you can easily set up and interact with the Dockerized multi-container application, and you can use DBeaver to inspect and manipulate the database directly.