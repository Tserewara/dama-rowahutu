from __future__ import annotations
import abc
from typing import Optional
from . import exceptions
from .encryptor import Encryptor, AbstractEncryptor
from ..values.password import Password


class AbstractCredential(abc.ABC):
    username: str
    password: str
    active: bool

    @classmethod
    @abc.abstractmethod
    def factory(
            cls,
            username: str,
            password: str,
    ) -> Credential:
        raise NotImplementedError

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

    @property
    def password(self):
        return self._password.value

    def __eq__(self, other: Credential) -> bool:
        return (self.username == other.username and
                self._password.value == other.password)

    @classmethod
    def factory(
            cls,
            username: str,
            password: Optional[str] = None,
            active: Optional[bool] = True
    ) -> AbstractCredential:
        if not username:
            raise exceptions.CredentialValueError('All arguments are required')

        _credential = cls(
            username=username,

            active=active
        )
        _credential.set_password(password)
        return _credential

    def set_password(self, value: str):
        self._password.value = value

    def verify_password(self, value: str) -> bool:
        return self._password == value

    def deactivate(self):
        self.active = False
