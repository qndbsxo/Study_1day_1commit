# Understanding Docker Concepts

Docker, an open-source project launched in 2013, has helped popularize technology and has helped drive the trend towards containerization and micro services in software development that's known as cloud-native development.

# What is Virtualization?

Virtualization is the technique of importing a Guest operating system on top of a Host operating system. This technique was a revelation at the beginning because it allowed developes to run many operating system in different virtual machines, all running on the same host. These eliminated the need for extra hardware resources.

# What is Containerization

Containerization is a form of operating system virtualization, through which it runs applications in secluded user spaces called containers, all using the same shared operating systems (OS).

# What is Docker
Docker is a tool designed to make it easier to create, deploy, and run application by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. Initially, built for Linux, Docker now runs on Windows and macOS. To understand how Docker works, let's look at some components you would use to create Docker-containerized applications.

# Docker Terms and Tool
Some of the tools and terminology you'll encounter when using Docker include the following:

- DockerFile: A DockerFile is a textfile that contains instructions on how to build a docker image, A Dockerfile specifies the operating system that will underlie the container, along with the languages, environmental variables, file locations, network ports, and other components it needs-and what the container will do once we run it.
- Docker Images: Docker images contain executable application source code as well as all the tools, libraries, and dependencies that the application code needs to run as a container, When you run the Docker image, it become one instance (or multiple instances) of the container.
- Docker Container: A Docker container image is a lightweight, standalone, executable package of software that has everything you need to run an application - code, runtime, system tools, system libraries, and settings.
- Docker Hub: Docker Hub is the public repository of Docker images that calls itself the "world's largest library and community for container images." It hold over 100,000 container images sourced from commercial software vendors, open-source projects, and individual developers. It includes images that have been produced by Docker, Inc., certified images belonging to the Docker Trusted Registry, and many thousands of other images. All Docker Hub users can share their images at will. They can also download predefined base images to use as a starting point for any containerization project.
- Docker Daemon: Docker Daemon is the background service running on the host that manges the building, running, and distributing Docker containers. The daemon is the process that runs in the operating system in which client speak.
- Docker Engine: Docker Engine is a client-server application that supports the task and
workflows involved to build, ship, and run container-based application. The engine creates a server-side daemon process that hosts images, containers, networks, and storage volumes.
- Docker Registry: The Docker Registry is where Docker Images are stored. The Registry can be either a user's local repository or a public repository like a Docker Hub allowing multiple users to collaborate in building an application. Even with several teams within the same organization can exchange or share containers by uploading them to Docker Hub, which is a cloud repository similar to GitHub
- Docker Compose: Docker-compose is for running multiple containers as a single service. It does so by running each container in isolation but allowing the containers to interact with one another.
- **Docker Swarm: Docker swarm is a service for containers that allows IT administrators and developers to create and manage a cluster of swarm nodes within the Docker platform. Each node of Docker swarm is a Docker daemon, and all Docker daemons interact using the Docker API. A swarm consists of two types of node: a manager node and a worker node. A manage node maintains cluster management tasks. Worker nodes receive and execute task from the manager node.

