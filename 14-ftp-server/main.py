import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # Instantiate a dummy authorizers for managing 'virtual users'
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user(
        username='demo',
        password='1234',
        homedir='/home/h404/Public/',
        perm='elradfmwMT',
        msg_login="Login Successful",
        msg_quit="Goodbye"
    )
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer=authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "ftpd ready"

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address, handler)

    # Set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # Start ftp server
    server.serve_forever()


if __name__ == "__main__":
    main()
