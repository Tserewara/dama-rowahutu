from __future__ import annotations
import abc
from typing import Optional
from . import exceptions


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
            password: Optional[str] = None,
            active: Optional[bool] = True
    ):
        self.username = username
        self.password = password
        self.active = active

    def __eq__(self, other: Credential) -> bool:
        return (self.username == other.username and
                self.password == other.password)

    @classmethod
    def factory(
            cls,
            username: str,
            password: Optional[str] = None,
            active: Optional[bool] = True
    ) -> AbstractCredential:
        if not username:
            raise exceptions.CredentialValueError('All arguments are required')

        return cls(
            username=username,
            password=password,
            active=active
        )

    def set_password(self, value: str):
        self.password = value

    def verify_password(self, value: str) -> bool:
        return self.password == value

    def deactivate(self):
        self.active = False
