# FastAPI and Vue

Repo just for test


## Getting started

Run with `make run`

Tests: `make test`



## Frontend

```bash
npx eslint --fix src/components/*.vue
```


## kube

```bash
cd infra

# first run/install
helm install fastapi-vue ./helm-chart

# update
helm upgrade fastapi-vue ./helm-chart
```
