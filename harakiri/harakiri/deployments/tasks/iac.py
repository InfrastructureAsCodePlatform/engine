from harakiri.core.ddocker import DDocker
from harakiri.core.manager import register
from harakiri.deployments.models import History
from harakiri.deployments.tasks.deployment import Deployment


@register()
class IaC(Deployment):
    abstract = True

    def execute(self, history: History, path: str, tempdir: str):
        logs, outputs = self.apply_boilerplate(history, path)
        history.modify(outputs=outputs, logs=logs)
        history.deployment.modify(outputs=outputs)

    def apply_boilerplate(self, history: History, path: str):
        boilerplate = history.deployment.boilerplate
        ddocker = DDocker(
            image=boilerplate.docker_image,
            command=["/bin/sh", "-c", f"{boilerplate.docker_command}"],
            environment=history.deployment.credential.credentials,
            container_dir=boilerplate.docker_directory,
            external_dir=path,
        )
        logs = ddocker.run()

        from harakiri.deployments.configs import LOGGERS

        outputs = LOGGERS[boilerplate.subtype](logs).get_outputs()
        return logs, outputs


if __name__ == "__main__":
    job = IaC()
    job.run()
