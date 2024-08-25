from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from config import PATH_x


# Настройка авторизации
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", PATH_x, perm="elradfmw")

# Настройка обработчика FTP
handler = FTPHandler
handler.authorizer = authorizer

# Запуск сервера
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
