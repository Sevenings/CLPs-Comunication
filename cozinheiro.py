from pycomm3 import SLCDriver
from ping3 import ping

class ConexaoCLP:
    def __init__(self, ip: str, tag_addr: str) -> None:
        self.ip = ip
        self.tag_addr = tag_addr

    def __connect(self):
        return SLCDriver(self.ip)

    def status(self):
        if ping(self.ip, timeout=2):
            return True
        return False

    def read(self):
        with self.__connect() as conexao:
            status = conexao.read(self.tag_addr)
        if status.error:
            return status.error
        return status.value

    def write(self, value):
        with self.__connect() as conexao:
            resultado = conexao.write((self.tag_addr, value))
        if resultado.error:
            return resultado.error
        print('Tag', resultado.tag)
        print('Value', resultado.value)
        print('Type', resultado.type)
        return resultado.value

    def __str__(self) -> str:
        return f'IP: {self.ip} | Bit: {self.tag_addr}'

