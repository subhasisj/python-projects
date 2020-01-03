import os
cwd = os.getcwd()

print('current:',cwd)

files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))