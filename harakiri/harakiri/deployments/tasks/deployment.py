import shutil
import tempfile

from celery import Task
from cookiecutter.main import cookiecutter
from retry import retry

from harakiri.core.models import STATUS
from harakiri.deployments.models import History


class Deployment(Task):
    abstract = False

    @retry(tries=5, delay=2)
    def get_history(self, history_id) -> History:
        return History.objects.get(id=history_id)

    def run(self, history_id=None, *args, **kwargs) -> None:
        tempdir = tempfile.mkdtemp()
        history = self.get_history(history_id)
        try:
            history.modify(status=STATUS.processing)
            path = self.get_boilerplate(history, tempdir)
            self.execute(history, path, tempdir)
            history.modify(status=STATUS.completed)
        except Exception as e:
            shutil.rmtree(tempdir)
            history.modify(msg=str(e), status=STATUS.failed)

    def get_boilerplate(self, history: History, tempdir: str):
        boilerplate = history.deployment.boilerplate
        return cookiecutter(
            template=boilerplate.url,
            output_dir=tempdir,
            directory=boilerplate.path,
            no_input=True,
            extra_context=history.inputs,
        )

    def execute(self, history: History, path: str, tempdir: str):
        ...


if __name__ == "__main__":
    job = Deployment()
    job.run()
