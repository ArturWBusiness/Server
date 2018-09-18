import os
directory = os.getcwd()
dirs = [x[0] for x in os.walk(directory)]
temp_dir = []
for path in dirs:
    temp_dir.append(
        path.split("\\")[0]
    )
