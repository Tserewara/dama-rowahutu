import pytest

from src.articles.domain.entities import exceptions, encryptor


class TestEncrypt:

    def test_raises_encryptor_type_error_when_param_is_not_a_string(self):
        with pytest.raises(exceptions.EncryptorTypeError):
            encryptor.Encryptor.encrypt(None)

    def test_returns_string(self):
        assert isinstance(encryptor.Encryptor.encrypt('password'), str)


class TestVerify:

    def test_returns_false_encrypted_value_is_different(self):
        encrypted_value = encryptor.Encryptor.encrypt('password@123')
        value = 'password'

        assert encryptor.Encryptor.verify(value, encrypted_value) is False

    def test_returns_true_when_encrypted_value_is_equal(self):
        value = 'password'
        encrypted_value = encryptor.Encryptor.encrypt(value)

        assert encryptor.Encryptor.verify(value, encrypted_value)
