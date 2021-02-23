from __future__ import annotations
import abc
from typing import Optional
from uuid import UUID, uuid4


class CredentialValueError(Exception):
    pass


class AbstractCredential(abc.ABC):

    @abc.abstractmethod
    def uuid(self) -> UUID:
        raise NotImplementedError

    @abc.abstractmethod
    def username(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def password(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def active(self):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def factory(
            cls,
            user_id: UUID,
            username: str,
            password: str,
            uuid: Optional[UUID] = None
    ) -> Credential:
        raise NotImplementedError

    @abc.abstractmethod
    def set_password(self, value: str):
        raise NotImplementedError


class Credential(AbstractCredential):

    def __init__(
            self,
            uuid: UUID,
            username: str,
            password: Optional[str] = None,
            active: Optional[bool] = True
    ):
        self._uuid = uuid
        self._username = username
        self._password = password
        self._active = active

    def __eq__(self, other: Credential) -> bool:
        return (self.username == other.username and
                self._password == other._password)

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def active(self) -> bool:
        return self._active

    @classmethod
    def factory(
            cls,
            username: str,
            password: Optional[str] = None,
            uuid: Optional[UUID] = None,
            active: Optional[bool] = True
    ) -> AbstractCredential:
        uuid = uuid or uuid4()

        if not all([username, password]):
            raise CredentialValueError('All arguments are required')

        return cls(
            uuid=uuid,
            username=username,
            password=password,
            active=active
        )

    def set_password(self, value: str):
        self._password = value
