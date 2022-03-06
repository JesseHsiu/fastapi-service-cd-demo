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


## Foleder Structure
```
.
├── app                  # application files
│   ├── cronjobs         # cronjob scripts
│   ├── cruds            # every db transaction methods
│   ├── migrations       # db migration (alembic)
│   ├── models           # db models
│   ├── routers          # routers for different prefix endpoint
│   ├── schemas          # response schemas (for documentation)
│   ├── utils            # common functions
│   ├── config.py        # application settings (derived from dot_envs)
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

