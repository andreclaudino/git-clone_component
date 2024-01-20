from kfp import dsl
from kubernetes.client import V1EnvVar, V1SecretKeySelector, V1EnvVarSource

from git_clone.constants import GIT_TOKEN_ENV, GIT_USERNAME_ENV


def setup_environment_variables(operator: dsl.ContainerOp, credentials_secret: str, username_key: str, token_key: str) -> dsl.ContainerOp:
    operator = _add_env_from_secret(operator, credentials_secret, GIT_USERNAME_ENV, username_key)
    operator = _add_env_from_secret(operator, credentials_secret, GIT_TOKEN_ENV, token_key)
    
    return operator


def _add_env_from_secret(operator: dsl.ContainerOp, secret_name: str, env_name: str, secret_key: str) -> dsl.ContainerOp:
    operator.container.add_env_variable(V1EnvVar(
        name=env_name,
        value_from=V1EnvVarSource(
            secret_key_ref=V1SecretKeySelector(
                name=secret_name,
                key=secret_key
            )
        )
    ))
    return operator