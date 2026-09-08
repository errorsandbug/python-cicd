import os
import shutil


SOURCE = "app.py"
DEPLOY_FOLDER = "deployment"


def deploy():

    print("Starting deployment...")

    if not os.path.exists(DEPLOY_FOLDER):
        os.makedirs(DEPLOY_FOLDER)

    shutil.copy(SOURCE, DEPLOY_FOLDER)

    print("Application deployed successfully!")


if __name__ == "__main__":
    deploy()