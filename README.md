# Service CI/CD Demo
This repository is an example of a starting point of every project we have: including Steaker / XY Finance / Galaxy Kats.

Some highlights here:
- Infrastructure as code
- CI / CD built in
- Fast API with auto documentation / schema
- Environment variable
- Folder structure guidelines
- Use `pipenv` to manage packages

## Cluster requirements
- Install NGINX Ingress Controller (https://kubernetes.github.io/ingress-nginx/deploy/)

## Foleder Structure
```
.
├── test                    # Test files (alternatively `spec` or `tests`)
│   ├── benchmarks          # Load and stress tests
│   ├── integration         # End-to-end, integration tests (alternatively `e2e`)
│   └── unit                # Unit tests
└── ...
```

