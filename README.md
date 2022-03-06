# FastAPI with SQL database demo
This repository is an example of a starting point of every project we have: including Steaker / XY Finance / Galaxy Kats.

## Highlights:
- Folder structure guidelines
- Fast API with auto documentation / schema
- Use `pipenv` to manage packages
- Use `alembic` to manage DB migrations
- Infrastructure as code in `k8s`
- CI / CD built in
- Environment variable to application


## Usage
- Clone this repo
- Setup environment variables in CircleCI
  - Based on your conditions, setup the followings: `GCLOUD_SERVICE_KEY`, `GOOGLE_COMPUTE_REGION`, `GOOGLE_COMPUTE_ZONE`, `GOOGLE_PROJECT_ID`, `K8S_CLUSTER_NAME_STAGE`, `K8S_CLUSTER_NAME_INTERNAL`, `K8S_CLUSTER_NAME_PROD` (as described in `.circleci/config.yml`)
- Database should use Cloud SQL, and connect by [Auth Proxy](https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine) as side-car in your deployment
- `internal` environmemnt is optional, please make changes based on your requirements

## Environments
- `stage`: testing environments with test configurations (such as testnet, test erc20 ...etc)
- `internal` (optional): same as production environment but limited access to internal
- `prod`: production environment and GA (general available)

## Lifecycle of a feature
  - Create a branch from `main`, named it as JIRA ticket name (such as `SJP-100`)
  - After implementation, create a PR to merge to `stage`
  - After reviews, merge it to `stage` (deployed to `stage` environment)
  - Check everything is ok in `stage` and should be tested by PM or QA
  - Create another PR from `SJP-100` to `main` & merge. (deployed to `internal` environment)
  - Check again if there is any issues in `internal`
  - Wait for release time and create a new release from github page (deployed to `prod` environment)
  - After some point or after release, merge `main` to `stage` or delete `stage` and create a new `stage` from `main` based on your conditions
  

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

