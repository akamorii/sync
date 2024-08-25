from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# Настройка авторизации
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "C:/Users/ineve/OneDrive/Рабочий стол/ftp_se", perm="elradfmw")

# Настройка обработчика FTP
handler = FTPHandler
handler.authorizer = authorizer

# Запуск сервера
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
