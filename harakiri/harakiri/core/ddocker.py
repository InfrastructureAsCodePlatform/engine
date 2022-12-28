import docker


class DDocker:
    def __init__(self, image: str, command: list[str], environment: dict, container_dir: str, external_dir: str):
        self.client = docker.from_env()
        self.image = image
        self.command = command
        self.environment = environment
        self.container_dir = container_dir
        self.external_dir = external_dir
        self.logs = None

    def run(self):
        return self.client.containers.run(
            image=self.image,
            command=self.command,
            environment=self.environment,
            volumes={
                self.external_dir: {
                    "bind": self.container_dir,
                    "mode": "rw",
                }
            },
            remove=True,
        ).decode("utf-8")
