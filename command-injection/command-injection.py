import os

filename = input("Please provide a file name to search and display:\n")

# to protect the code from being hacked use the code below
if filename == os.path.basename(__file__):
	# checks if filename is the current file or not
	print("filename cannot be the current running file")
	os._exit(0)

command = "cat " + filename
os.system(command)
