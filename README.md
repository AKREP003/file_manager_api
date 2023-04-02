API for file_manager

first import the Client:

from file_manager_api import Client

To create a client:

Client = Client(*url for the service, *your user name, *your password)

To create a file:

Client.write_file(<new file name>,  <content>) #content is optional when creating a new file

To list the existing files:

Client.list_files

To read a file:

Client.read_file(<file name>)

To write into a file:

Client.read_file(<file name>, <content>) #content is optional when you want to empty the file
