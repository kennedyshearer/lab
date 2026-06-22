# Dad Joke Dashboard - Multi-Container Docker Application

A containerized live dashboard built with Docker Compose that automatically fetches and displays new dad jokes every 30 seconds.

This project was created to practice building multi-container applications, container communication, Docker volumes, security best practices, and service separation.

## Overview

The application consists of two independent containers working together:

1. **Updater Container** - A Bash-based service that fetches dad jokes from an external API and generates an HTML dashboard.
2. **Web Container** - An nginx service that serves the generated dashboard to users.

Both containers communicate through a shared Docker volume that stores the generated HTML content.

## Architecture

```
                     Docker Compose

        +--------------------------------+
        |                                |
        |      Updater Container         |
        |                                |
        |  Bash Script                   |
        |  - Fetch dad joke API          |
        |  - Generate HTML               |
        |  - Update dashboard            |
        |                                |
        +---------------+----------------+
                        |
                        |
                        v
                 Shared Volume
                    /html

                        |
                        |
                        v

        +---------------+----------------+
        |                                |
        |       nginx Container          |
        |                                |
        |  - Serve static HTML           |
        |  - Listen on port 8080         |
        |                                |
        +---------------+----------------+

                        |
                        |
                        v

                 User Browser
```

## How It Works

### Updater Container

The updater service runs a Bash script that:

* Calls the `icanhazdadjoke` API
* Retrieves a random dad joke
* Generates an HTML dashboard
* Writes the output to `/html/index.html`
* Repeats every 30 seconds

The container is designed with a single responsibility: generating application content.

### nginx Container

The nginx container is responsible for serving the dashboard.

Instead of combining content generation and web serving into one container, these responsibilities are separated:

* The updater creates the content
* nginx delivers the content

This keeps each service lightweight and easier to maintain.

### Shared Volume

The containers communicate through a Docker-managed volume:

```
Updater Container
        |
        |
        v
/html/index.html
        |
        |
        v
nginx Container
```

The updater writes the generated HTML file, and nginx reads the same file to serve the dashboard.

## Technologies Used

* Docker
* Docker Compose
* Docker Volumes
* Bash
* nginx
* Linux
* HTML/CSS
* REST API Integration

## Project Structure

```
joke-dashboard/
├── docker-compose.yaml
├── Dockerfile.update
├── updater
└── README.md
```

## Running the Application

### Clone Repository

```bash
git clone <repository-url>
cd dad-joke-dashboard
```

### Build and Start Containers

```bash
docker compose up -d --build
```

### Verify Running Containers

```bash
docker compose ps
```

### Access Dashboard

Open:

```
http://localhost:8080
```

The dashboard will automatically update with a new joke every 30 seconds.

## Container Security Practices

This project incorporates several container best practices:

### Non-Root Containers

The updater container runs using a non-root user to reduce unnecessary privileges.

The nginx service uses the `nginx-unprivileged` image to avoid running the web server as root.

### Volume Permission Management

Because both containers share access to the same volume, permissions must be handled correctly.

An initialization container is used to prepare volume ownership before the application starts:

```yaml
init:
  command: chown -R 101:101 /html
```

This ensures the updater container can write generated content while maintaining a non-root execution model.

## Key Takeaways

This project reinforced the importance of designing containers around clear responsibilities.

Instead of building one large container that handles everything, the application was separated into smaller services that work together:

* One container creates the content
* One container serves the content
* A shared volume connects the services

Building this application provided hands-on experience with Docker Compose, container communication, Linux scripting, nginx, persistent storage, and container security practices.

