import re

from src.articles.domain.entities import exceptions
from src.articles.domain.entities.encryptor import AbstractEncryptor


class Password:

    def __init__(self, encryptor: AbstractEncryptor, value: str = None):
        self._encryptor = encryptor
        self._value = value

    def __repr__(self):
        return '<Password object {}>'.format(self._value)

    def __eq__(self, value: str) -> bool:
        return self._encryptor.verify(value, self._value)

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def validate_strength(cls, value: str) -> (bool, dict):
        """
        Verify the strength of 'password', it returns a dict with
        bool values for each validation.

        A password is considered strong if:
            8 characters length or more
            1 digit or more
            1 symbol or more
            1 uppercase letter or more
            1 lowercase letter or more
        """

        if value is None:
            return False, {}

        length = cls._is_longer_than_7(value)
        digit = cls._has_digit(value)

        is_valid = all([length, digit])
        error_dict = {
            'length': length,
            'digit': digit
        }

        return is_valid, error_dict

    @classmethod
    def _is_longer_than_7(cls, value):
        return not len(value) < 8

    @classmethod
    def _has_digit(cls, value):
        return bool(re.search(r"\d", value))

    @value.setter
    def value(self, value: str):
        valid_password, _ = self.validate_strength(value)
        if not valid_password:
            raise exceptions.PasswordStrengthError(
                'A strong password should contain at least 8 characters, '
                '1 digit, 1 symbol, 1 uppercase letter, and 1 lowercase '
                'letter'
            )
        self._value = self._encryptor.encrypt(value)
