from __future__ import annotations
import abc

from src.articles.domain.entities import exceptions
from src.articles.domain.entities.encryptor import Encryptor, AbstractEncryptor
from src.articles.domain.values.password import Password


class AbstractCredential(abc.ABC):
    username: str
    password: str
    active: bool

    @abc.abstractmethod
    def set_password(self, value: str):
        raise NotImplementedError

    @abc.abstractmethod
    def verify_password(self, value: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def deactivate(self):
        raise NotImplementedError


class Credential(AbstractCredential):

    def __init__(
            self,
            username: str,
            password: str = None,
            encryptor: AbstractEncryptor = Encryptor,
            active: bool = True
    ):
        self.username = username
        self._password = Password(encryptor, password)
        self.active = active

        if self.username is None:
            raise exceptions.CredentialValueError('All arguments are required')

    @property
    def password(self):
        return self._password.value

    def set_password(self, value: str):
        self._password.value = value

    def __eq__(self, other: Credential) -> bool:
        return (self.username == other.username and
                self._password.value == other.password)

    def verify_password(self, value: str) -> bool:
        return self._password == value

    def deactivate(self):
        self.active = False


if __name__ == '__main__':
    c1 = Credential('Tserewara')

    c1.set_password('Password1')

    print(c1.password)
    print(c1.verify_password('Password1'))
