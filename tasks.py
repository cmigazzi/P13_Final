import os

from fabric2 import Connection
from invoke import task, Responder          

REPO_URL = "https://github.com/cmigazzi/P13_Final.git"
SITE_FOLDER = os.environ.get("SITE_FOLDER")
SUPERVISOR_CONF = os.environ.get("SUPERVISOR_CONF")


@task
def deploy(c):
    c = Connection(os.environ.get("SSH_ADDRESS"), connect_kwargs={"passphrase": os.environ.get("PASSPHRASE")})
    c.run(f"mkdir -p {SITE_FOLDER}")
    with c.cd(f"{SITE_FOLDER}"):
        _get_latest_sources(c)
        _update_pipenv(c)
        _update_staticfiles(c)
        _update_migrations(c)


def _get_latest_sources(c):
    directories = c.run(f"ls -a", hide="out")
    if ".git" not in directories.stdout:
        c.run(f"git clone {REPO_URL} .")
    else:
        c.run("git pull origin master")


def _update_pipenv(c):
    venv_path = c.run("pipenv --venv", warn=True)
    if venv_path.failed:
        c.run("pipenv install")
    else:
        c.run("pipenv sync")


def _update_staticfiles(c):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    c.run(f"export SECRET_KEY='{SECRET_KEY}' && "
          f"export DJANGO_SETTINGS_MODULE='core.settings.production' && "
          f"pipenv run python manage.py collectstatic --no-input")


def _update_migrations(c):
    DATABASE_URL = os.environ.get("DEPLOY_DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    c.run(f"export SECRET_KEY='{SECRET_KEY}' && "
          f"export DJANGO_SETTINGS_MODULE='core.settings.production' && "
          f"export DATABASE_URL='{DATABASE_URL}' && "
          f"pipenv run python manage.py migrate")


@task()
def merge_to_master(localhost, branch):
    localhost.run("git checkout master")
    localhost.run(f"git merge {branch}")
    localhost.run("git push origin master")
