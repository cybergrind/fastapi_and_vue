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


#### Certificates

```bash
# **NOTE**: set CN to registry.kube.zz
mkdir -p infra/certs
cd infra

openssl req \
  -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key \
  -addext "subjectAltName = DNS:registry.kube.zz" \
  -x509 -days 10365 -out certs/domain.crt

kubectl create secret tls registry-tls --cert=./infra/certs/domain.crt --key=./infra/certs/domain.key

kubectl create secret generic registry-ca --namespace fastapi-vue --from-file=registry-ca=./infra/certs/domain.crt
kubectl create secret generic registry-ca --namespace fastapi-vue --from-file=registry-key=./infra/certs/domain.key
```
