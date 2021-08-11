import os
import shutil
root_dir = "my_project"
for root, dirs, files in os.walk(root_dir):
    if "templates" in dirs and root != root_dir:
        for i in os.listdir(os.path.join(root, "templates")):
            shutil.copytree(os.path.join(root, "templates", i), os.path.join(root_dir, "templates", i))
