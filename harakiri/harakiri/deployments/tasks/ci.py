import shutil
import tempfile

from git import Repo

from harakiri.core.manager import register
from harakiri.deployments.models import History
from harakiri.deployments.tasks.deployment import Deployment


@register()
class CI(Deployment):
    abstract = True

    def execute(self, history: History, path: str, tempdir: str):
        source = history.deployment.source
        tempdir2 = tempfile.mkdtemp()
        try:
            repo = Repo.clone_from(source.repository_auth_url, tempdir2)

            if source.branch:
                repo.git.checkout(source.branch)

            path = f"{tempdir}/{history.inputs['project_id']}-{history.inputs['deployment_id']}"
            shutil.copytree(path, tempdir2, dirs_exist_ok=True)

            if repo.untracked_files or [item.a_path for item in repo.index.diff(None)]:
                repo.git.add(all=True)
                repo.index.commit("Configure CI for the project.")
                origin = repo.remote(name="origin")
                origin.push()
        finally:
            shutil.rmtree(tempdir2)


if __name__ == "__main__":
    job = CI()
    job.run()
