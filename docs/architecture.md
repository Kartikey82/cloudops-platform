
# CloudOps Platform Architecture

## Current Architecture

The application is developed locally and published to GitHub.

1. **FastAPI** exposes REST endpoints.
2. **Uvicorn** serves HTTP requests.
3. **Docker** packages the application and its runtime dependencies.
4. **GitHub** stores the source code and commit history.
5. **GitHub Actions** runs automated tests on pushes and pull requests.

## Request Flow

```text
Client
  |
  v
Docker host port 8000
  |
  v
FastAPI / Uvicorn container
  |
  v
JSON response
```

## Continuous Integration Flow

```text
Developer changes code
        |
        v
Git commit and push
        |
        v
GitHub Actions workflow
        |
        v
Install development dependencies
        |
        v
Run pytest
        |
        v
Pass or fail result
```

## Planned Cloud Architecture

Future infrastructure will be designed with cost and security constraints
in mind. Potential components include:

- Terraform for infrastructure as code
- AWS IAM for controlled access
- A container deployment target, if eligible at zero cost
- Centralized logs and health monitoring
- CI checks for infrastructure and application changes

These are planned components, not currently deployed AWS resources.

## Current Limitations

- The service has not been deployed to AWS.
- The readiness endpoint does not yet check external dependencies.
- Production authentication, rate limiting, and secrets management are not implemented.
- Dependency and container vulnerability scanning is not yet configured.
