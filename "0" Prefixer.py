#! python3
# FG #8 '0 Prefixer'.py - Adds "0" to the beginning of the filename of
# all .txt files in the current working directory.

import os

# Lists all files in the current working directory.
cwd = os.listdir(os.getcwd())

# Adds 0 before the filename for .txt files.
for file in cwd:
    if not file.endswith('.txt'):
        continue

    newname = '0' + file

    # Commented for safety. Uncomment to use.
    # os.rename(file, newname)
