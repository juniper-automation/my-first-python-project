import os
from invoke import task

### ---------------------------------------------------------------------------
### DOCKER PARAMETERS
### ---------------------------------------------------------------------------
DOCKER_IMG = "odb"
DOCKER_TAG = "latest"

### ---------------------------------------------------------------------------
### SYSTEM PARAMETERS
### ---------------------------------------------------------------------------
PWD = os.getcwd()

### ---------------------------------------------------------------------------
### DOCKER CONTAINER BUILD
### ---------------------------------------------------------------------------
@task
def build(context):
    # Build our docker image
    context.run(
        f"docker build -t {DOCKER_IMG}:{DOCKER_TAG} .",
    )

### ---------------------------------------------------------------------------
### DOCKER CONTAINER SHELL
### ---------------------------------------------------------------------------
@task
def shell(context):
    # Get access to the BASH shell within our container
    print("Jumping into container, type exit to return to host")
    context.run(
        f"docker run -it --rm \
            -v {PWD}/:/home/python \
            -w /home/python/ \
            {DOCKER_IMG}:{DOCKER_TAG} /bin/bash",
        pty=True,
    )


### ---------------------------------------------------------------------------
### EXECUTE PYTHON SCRIPT FROM WITHIN CONTAINER
### ---------------------------------------------------------------------------
@task
def script(context):
    # Execute Ansible playbook from within the container
    context.run(
        f"docker run -it \
            --rm \
            -v {PWD}/:/home/python \
            -w /home/python/ \
            {DOCKER_IMG}:{DOCKER_TAG} python app.py",
        pty=True,
    )
