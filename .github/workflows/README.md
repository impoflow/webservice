# Deployment Tests

**Workflow Name:** Test Deployment
This workflow is triggered on pushes to the main and develop branches and on pull requests to the main branch. It performs the following steps:

- Checkout Code: Clones the repository.
- Modify Client Configuration: Updates the client to accept localhost connections.
- Mock Environment Variables: Defines placeholders for bucket and region values.
- Install Docker Compose: Ensures the required version is available.
- Run Docker Compose: Starts all services using mocked environment variables.
- Build and Start Containers: Builds and runs the Docker containers, displaying logs for debugging.
- Stop and Clean Up: Shuts down and removes orphaned containers.


```mermaid
graph TD;
    A[Push or Pull Request to Main/Develop] --> B[Checkout Code];
    B --> C[Modify Client Configuration];
    C --> D[Mock Environment Variables];
    D --> E[Install Docker Compose];
    E --> F[Run Docker Compose];
    F --> G[Build and Start Containers];
    G --> H[Stop and Clean Up];

    subgraph Test Deployment Workflow
        B -->|Clone Repo| C;
        C -->|Modify client/script.js| D;
        D -->|Set BUCKET_NAME, REGION| E;
        E -->|Download & Set Permissions| F;
        F -->|Start Services| G;
        G -->|Docker Logs| H;
    end
```

# Unit Tests

**Workflow Name:** Run Unit Tests
This workflow is triggered on pushes to the main and develop branches and on pull requests to the main branch. It performs the following steps:

- Checkout Code: Clones the repository.
- Set up Python: Installs Python 3.11.
- Install Dependencies: Installs required packages for API and file handlers.
- Set PYTHONPATH: Configures the environment for module discovery.
- Run Tests with Coverage: Executes tests for API and file handlers, generating coverage reports.
- Upload Coverage Reports: Saves the coverage reports as artifacts for further analysis.

```mermaid
graph TD;
    A[Push or Pull Request to Main/Develop] --> B[Checkout Code];
    B --> C[Set up Python 3.11];
    C --> D[Install Dependencies];
    D --> E[Set PYTHONPATH];
    E --> F[Run ApiHandler Tests with Coverage];
    F --> G[Run FileHandler Tests with Coverage];
    G --> H[Upload Coverage Reports];

    subgraph Unit Tests Workflow
        B -->|Clone Repo| C;
        C -->|Install Python 3.11| D;
        D -->|Install requirements| E;
        E -->|Configure Environment| F;
        F -->|Run unittest with Coverage| G;
        G -->|Store Coverage Reports| H;
    end

```
