# Service CI/CD Demo
This repository is an example of a starting point of every project we have: including Steaker / XY Finance / Galaxy Kats.

## Highlights:
- Folder structure guidelines
- Fast API with auto documentation / schema
- Use `pipenv` to manage packages
- Use `alembic` to manage DB migrations
- Infrastructure as code in `k8s`
- CI / CD built in
- Environment variable to application


## Folder Structure
```
.
├── app                  # application files
│   ├── cronjobs         # cronjob scripts (regularly update by workers...etc)
│   ├── cruds            # DB transaction methods (create, read, update and delete)
│   ├── migrations       # DB migration (alembic)
│   ├── models           # DB models
│   ├── routers          # Routers for different prefix endpoint
│   ├── schemas          # Response schemas (for documentation)
│   ├── utils            # Common functions
│   ├── config.py        # Application settings (derived from dot_envs)
│   ├── database.py      # Databse instance
│   └── main.py          # FastAPI instance
├── dot_envs             # dot env for different environment
├── k8s                  # K8s related files
│   ├── base             # Load and stress tests
│   └── overlays         # Unit tests
├── scripts              # Some manually scripts to use
├── tests                # Test files
└── ...
```

