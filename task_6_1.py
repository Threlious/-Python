with open("nginx_logs.txt", 'r', encoding="utf-8") as file1:
    content = ((line.split()[0], line.split()[5].replace('"', ''), line.split()[6]) for line in file1)
    for i in content:
        print(i)
