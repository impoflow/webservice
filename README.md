# Webservice

This repository contains a web application that provides specific services through a client-server architecture.

---

## Project Structure

- **`client/`**: Source code for the client. This contains the user interface and functionalities that interact with the server.
- **`server/`**: Source code for the server. It handles incoming requests, processes the logic, and returns appropriate responses to the client.
- **`.github/workflows/`**: Configurations for continuous integration and deployment using GitHub Actions.
- **`docker-compose.yml`**: Configuration file to orchestrate the client and server services using Docker Compose.

---

## Technologies Used

- **Python**: Main language used for server development.
- **JavaScript**: Used on the client side for application interaction and dynamism.
- **Docker**: Facilitates application containerization and deployment.
- **GitHub Actions**: Implemented for continuous integration and deployment.

---

## Prerequisites

Before starting, make sure you have the following installed:

- **Docker**: Required to run the application's containers.
- **Docker Compose**: Used to manage and run multiple containers in an orchestrated way.

---

## Getting Started

### 1. **Clone the Repository**

Clone this repository to your local machine to access the source code:

```bash
git clone https://github.com/impoflow/webservice.git
cd webservice
```

---

### 2. **Review the Configuration**

Before starting the services, review the configurations to ensure they suit your environment:

1. **Check the ports**:
   - Verify the `docker-compose.yml` file to ensure the configured ports are not in use by other services.
   - By default, the client is configured to run on port `80`. If you need to use a different port, edit the corresponding lines in the `docker-compose.yml` file.

2. **Update the `client/scripts.js` file**:
   - Open the file located at `client/scripts.js`.
   - Replace `{backend_ip}` in the first two lines with `localhost`.

---

### 3. **Start the Services with Docker Compose**

Run the following command to build and start the containers:

```bash
docker-compose up --build
```

This command will:

- Build the Docker images specified in the `docker-compose.yml` file.
- Start the containers for the client and server.

---

### 4. **Access the Application**

Once the containers are running, you can access the client application in your browser.

By default, it will be available on port `80`. Open your browser and go to:

```
http://localhost
```

If you changed the port in the `docker-compose.yml` file, replace `80` with the configured port. For example, if the port is set to `8080`, visit:

```
http://localhost:8080
```

---

## Contributions

Contributions are welcome! Follow these steps to collaborate:

1. **Fork** the repository.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/new-feature
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add new feature"
   ```

4. Push your branch to the remote repository:

   ```bash
   git push origin feature/new-feature
   ```

5. Open a **Pull Request** on the original repository detailing your changes.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

**Note**: Before deploying the application in a production environment, ensure you review and adjust all configurations according to your specific needs.

---
