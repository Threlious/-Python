import os
list_of_files = ["settings", "mainapp", "adminapp", "authapp"]
for i in list_of_files:
    if not os.path.exists(os.path.join("my_project", i)):
        os.makedirs(os.path.join("my_project", i))
    else:
        print("Dirs already exist")
