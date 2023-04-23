API for file_manager

first import the Client:

from file_manager_api import Client

To create a client:

client = Client(*url for the service, *your user name, *your password)

To create a file:

client.write_file(*new file name, *content) #content is optional when creating a new file

To list the existing files:

client.list_files

To read a file:

client.read_file(*file name)

To write into a file:

client.write_file(*file name, *content) #content is optional in case you want to empty the file
