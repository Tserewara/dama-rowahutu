import pytest

from src.articles.domain.entities import encryptor, exceptions
from src.articles.domain.values.password import Password


class FakeEncryptor(encryptor.Encryptor):

    @classmethod
    def encrypt(cls, value):
        return value + 'encrypt'

    @classmethod
    def verify(cls, value, encrypted):
        return encrypted == value + 'encrypt'


class TestInit:

    def test_sets_value_without_encryption(self):
        password = Password(FakeEncryptor, 'password')
        assert password.value == 'password'

    def test_sets_value_to_none_when_password_is_not_passed(self):
        password = Password(FakeEncryptor)
        assert password.value is None


class TestPasswordValueSetter:

    def test_raises_password_strength_error_when_password_is_not_strong(self):
        with pytest.raises(exceptions.PasswordStrengthError):
            password_value = Password(FakeEncryptor)
            password_value.value = 'pass'

    def test_stores_password_encrypted_when_it_is_strong(self):
        password = 'StrongPass.10'
        password_value = Password(FakeEncryptor)
        password_value.value = password

        assert password_value.value != password


class TestValidateStrength:

    def test_returns_false_when_password_is_none(self):
        result, _ = Password.validate_strength(None)
        assert result is False

    def test_returns_false_on_dict_when_password_length_is_less_than_8(self):
        _, result = Password.validate_strength('pass')
        assert result.get('length') is False

    def test_returns_true_on_dict_when_password_length_is_greater_than_7(self):
        _, result = Password.validate_strength('password')
        assert result.get('length') is True

    def test_returns_false_on_dict_when_password_has_no_digit(self):
        _, result = Password.validate_strength('pass')
        assert result.get('digit') is False

    def test_returns_true_on_dict_when_password_has_digit(self):
        _, result = Password.validate_strength('password1')
        assert result.get('digit') is True


