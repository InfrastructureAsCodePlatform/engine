import os
import shutil

from git import Repo

from harakiri.core.manager import register
from harakiri.deployments.models import History
from harakiri.deployments.tasks.deployment import Deployment


@register()
class CI(Deployment):
    abstract = True

    def execute(self, history: History, path: str, tempdir: str):
        boilerplate = history.deployment.boilerplate
        repo = Repo.clone_from(boilerplate.url, tempdir)

        if boilerplate.branch:
            repo.git.checkout(boilerplate.branch)

        shutil.copytree(path, os.path.join(tempdir, boilerplate.url.split("/")[-1][0:-4]))

        repo.git.add(all=True)
        repo.index.commit("Configure CI for the project.")
        origin = repo.remote(name="origin")
        origin.push()


if __name__ == "__main__":
    job = CI()
    job.run()
