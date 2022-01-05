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


If you switch `backend.useExternal` you may need to edit endpoint

```bash
k edit endpoints fastapi-vue-backend

# and add
metadata:
  annotations:
    meta.helm.sh/release-name: fastapi-vue
    meta.helm.sh/release-namespace: fastapi-vue
```

#### Certificates

```bash
# **NOTE**: set CN to registry.kube.zz
cd infra

openssl req \
  -newkey rsa:4096 -nodes -sha256 -keyout helm-chart/domain.key \
  -addext "subjectAltName = DNS:registry.kube.zz" \
  -x509 -days 10365 -out helm-chart/domain.crt
```
