
from file_manager_api import Client


x = Client(server_url="http://localhost", username="admin", password="nevergonnagiveyouup")

print(x.read_file("flag.txt"))

print(x.list_files()[0])

x.write_file("flag.txt", "olo")

print(x.read_file("flag.txt"))

x.write_file("new_file", "www")

print(x.read_file("new_file"))




