from uuid import UUID, uuid4

import pytest

from src.articles.domain import credential


class TestFactory:

    def test_when_has_no_uuid_adds_uuid(self):
        my_credential = credential.Credential.factory('username', 'password')
        assert isinstance(my_credential.uuid, UUID)

    def test_when_has_uuid_keeps_what_was_set(self):
        uuid_value = uuid4()

        my_credential = credential.Credential.factory(
            'username',
            'password',
            uuid_value
        )

        assert my_credential.uuid == uuid_value

    def test_raises_credential_value_error_when_has_no_username(self):
        with pytest.raises(credential.CredentialValueError,
                           match='All arguments are required'):
            credential.Credential.factory(None, 'password', uuid4())

    def test_creates_credential_instance(self):
        my_credential = credential.Credential.factory(
            'username',
            'password',
            uuid4(),
        )

        assert isinstance(my_credential, credential.Credential)

    def test_keeps_password_value_when_is_passed(self):
        password = 'password'

        my_credential = credential.Credential.factory(
            'username',
            password,
            uuid4(),
        )

        assert my_credential.password == password


class TestCredentialProperties:

    def setup(self):
        uuid_value = uuid4()
        self.params = {
            "uuid": uuid_value,
            "username": "Tserewara",
            "password": "password",
            "active": True
        }

        self.credential = credential.Credential.factory(
            self.params['username'],
            self.params['password'],
            self.params['uuid'],
            self.params['active'],
        )

    def test_uuid(self):
        assert self.credential.uuid == self.params['uuid']

    def test_username(self):
        assert self.credential.username == self.params['username']

    def test_password(self):
        assert bool(self.credential.password)

    def test_active(self):
        assert not (self.credential.active is None)


class TestPasswordSetter:

    def test_set_password(self):
        uuid_value = uuid4()

        my_credential = credential.Credential.factory(
            'username',
            'password',
            uuid_value,
        )

        old_pass = my_credential.password
        my_credential.set_password('new_password')

        assert old_pass != my_credential.password


class TestCredentialEquality:

    def test_returns_false_when_username_is_different(self):
        uuid_value = uuid4()

        credential_a = credential.Credential.factory(
            'johndoe',
            'password',
            uuid_value
        )

        credential_b = credential.Credential.factory(
            'fulano',
            'password',
            uuid_value
        )

        assert credential_a != credential_b

    def test_returns_false_when_password_is_different(self):
        uuid_value = uuid4()

        credential_a = credential.Credential.factory(
            'johndoe',
            'password1',
            uuid_value
        )

        credential_b = credential.Credential.factory(
            'johndoe',
            'password2',
            uuid_value
        )

        assert credential_a != credential_b

    def test_returns_true_when_username_and_password_are_equal(self):
        uuid_value = uuid4()

        credential_a = credential.Credential.factory(
            'johndoe',
            'password',
            uuid_value
        )

        credential_b = credential.Credential.factory(
            'johndoe',
            'password',
            uuid_value
        )

        assert credential_a == credential_b
