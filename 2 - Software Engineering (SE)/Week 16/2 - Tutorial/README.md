# Jenkins Installation using Docker

## Overview
This guide provides step-by-step instructions to install Jenkins in a Docker container. Jenkins is a powerful open-source automation server that can be used for continuous integration and continuous delivery (CI/CD). Using Docker simplifies the setup and management process.

## Prerequisites
- **Docker**: Ensure you have Docker installed on your system. You can download and install Docker from [Docker's official website](https://docs.docker.com/get-docker/).
- If you don't have docker installed, you can use the playground [Docker Playground](https://labs.play-with-docker.com/)
- **Basic Docker Knowledge**: Familiarity with Docker commands and concepts is helpful.

## Installation guide
Please read through this document to get started [Jenkins Docker](https://www.jenkins.io/doc/book/installing/docker/).

You should be able by now to install things with the documentation. Once you are done with the installation, of Jenkins and the plugins, create your first freestyle project.

## Create a Docker cloud

- From the Jenkins welcome page, on the left corner click on **Manage Jenkins**
- Click on **Clouds**. The docker plugins might not be installed. Choose in the plugins **Docker** and **Docker-API**
- Click on **New Cloud**
- Put in the cloud name and select **Docker** and click on **Create**
- For the Docker URI: 
https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin

```bash
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
```
To get the IP of the new cloud master node

```bash
docker inspect <container_id> | grep IPAddress
```
- and enable the server
Then create a docker agent template. 

## Create a Project

You can choose between a **Freestyle** or a **Pipeline** project. 

### Create a Freestyle Project (Without a Docker agent)

- From the Jenkins welcome page, on the left corner click on **New Item**
- Enter the name of the project
- Click on **Freestyle Project**
- Click on **OK**
- In **Source Code Management**, click on Git and add the repo that has the code
- In the repository put in a the URL
- In **Branch Specifier (blank for 'any')** provide the actual branch name "main"
- In **Build Triggers**, choose **Poll SCM**
- In **Build Environment**, select **Delete workspace before build starts**
- In **Build Steps** add the step **Execute shell** and put in **python helloworld.py** or **python3 helloworld.py**
- Save and **Build Now**. Or because of **Poll SCM**, the build will get triggered after a change in the Git repository happens

## Create a cloud agent (Docker)

To run agent docker master node: 

https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin

```bash
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
```
To get the IP of the new cloud master node

```bash
docker inspect <container_id> | grep IPAddress
```

The executor node:

```bash
docker pull devopsjourney1/myjenkinsagents:python
```
The name of the image is **devopsjourney1/myjenkinsagents:python**
