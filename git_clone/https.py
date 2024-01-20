from kfp import dsl
from kubernetes import client as k8s


from git_clone.constants import DEFAULT_CONTAINER_NAME, DEFAULT_CPU_LIMIT, DEFAULT_CPU_REQUEST, DEFAULT_DISPLAY_NAME, DEFAULT_IMAGE_NAME, DEFAULT_IMAGE_TAG, DEFAULT_MEMORY_LIMIT, DEFAULT_MEMORY_REQUEST, OUTPUT_DIR, STARTUP_COMMAND
from git_clone.resources import setup_resources
from git_clone.secrets import setup_environment_variables
from git_clone.volumes import add_volume


def make_https_component(repository_url: str, credentials_secret: str, username_key: str, token_key: str, output_volume: k8s.V1Volume, output_subdirectory: str = "", 
                         display_name: str = DEFAULT_DISPLAY_NAME,
                         image_name: str = DEFAULT_IMAGE_NAME, image_tag: str = DEFAULT_IMAGE_TAG,
                         memory_request: str = DEFAULT_MEMORY_REQUEST, memory_limit: str = DEFAULT_MEMORY_LIMIT,
                         cpu_request: str = DEFAULT_CPU_REQUEST, cpu_limit: str = DEFAULT_CPU_LIMIT) -> dsl.ContainerOp:
    image = f"{image_name}:{image_tag}"

    base_repository_url = repository_url.split("://", 1)[1]
    clone_url = f"https://$(GIT_USERNAME):$(GIT_TOKEN)@{base_repository_url}"
    output_path = f"{OUTPUT_DIR}/{output_subdirectory}"

    operator = dsl.ContainerOp(
        name=DEFAULT_CONTAINER_NAME,
        image=image,
        command=STARTUP_COMMAND,
        arguments=[
            "clone",
            clone_url,
            output_path
        ]
    )

    operator = setup_environment_variables(operator, credentials_secret, username_key, token_key)
    operator = add_volume(output_volume, operator)
    operator = setup_resources(operator, memory_request, memory_limit, cpu_request, cpu_limit)

    operator.set_display_name(display_name)

    return operator




