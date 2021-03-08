import abc

from passlib.hash import bcrypt

from src.articles.domain.entities.exceptions import EncryptorTypeError


class AbstractEncryptor(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def encrypt(cls, value: str) -> str:
        pass

    @classmethod
    @abc.abstractmethod
    def verify(cls, value: str, encrypted: str) -> bool:
        pass


class Encryptor(AbstractEncryptor):

    @classmethod
    def encrypt(cls, value: str) -> str:
        if not isinstance(value, str):
            raise EncryptorTypeError('Value must be a string')

        return bcrypt.using(rounds=8).hash(value)

    @classmethod
    def verify(cls, value: str, encrypted: str) -> bool:
        return bcrypt.verify(value, encrypted)
