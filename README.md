# Git Clone Component

A component set to clone git repositories

## Available components

### Clone over HTTPs

```Python
from git_clone import make_https_component

git_clone_operator = make_https_component(
    repository_url=..., credentials_secret=..., username_key=...,
    token_key=..., output_volume=...)
```

#### Parameters

* `repository_url: str`: The https repository URL to be cloned, i.e: https://github.com/andreclaudino/git-clone_component.git
* `credentials_secret: str`: A kubernetes secret containing username and token/password keys
* `username_key: str`: The key for username in `credentials_secret`
* `token_key: str`, The key for token/password in `credentials_secret`
* `output_volume: k8s.V1Volume`: The kubernetes volume where repository data will be cloned
* `output_subdirectory: str`: The relative path for subdirectory inside volume where the data will be cloned into *(defaults to empty string, cloning into the volume root)*
  

## Common parameters over all components

* `display_name: str`: Component name to be displayed in Kubeflow or Argp UI (Defaults to "Git Clone")
* `image_name: str`: OCI image repository/name to be used in job (Defaults to "docker.io/bitnami/git")
* `image_tag: str` OCI image tag to be used in job (Defaults to "2.43.0")
* `memory_request: str`: Pod memory requested to Kubernetes (Defaults to 80Mi)
* `memory_limit: str`: Pod memory declared to Kubernetes (Defaults to 100Mi)
* `cpu_request: str`: Pod CPU requested to Kubernetes (Defaults to 100m)
* `cpu_limit: str`: Pod CPU declared to Kubernetes (Defaults to 200m)