import os

cwd = os.getcwd()
print(cwd)
with os.scandir(cwd) as it:
    for entry in it:
        if 'day' in entry.name and entry.is_file():
            start = entry.name.find('day')+3
            end = entry.name.find('_', start)
            folder_name = entry.name[start:end]
            folder_name = 'day'+folder_name
            os.makedirs(folder_name, exist_ok=True)
            replacement_name = cwd + "\\" + folder_name + '\\' + entry.name
            print(entry.path)
            os.replace(entry.path, replacement_name)
