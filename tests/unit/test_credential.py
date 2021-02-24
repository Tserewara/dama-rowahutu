import pytest

from src.articles.domain import credential


class TestFactory:

    def test_raises_credential_value_error_when_has_no_username(self):
        with pytest.raises(credential.CredentialValueError,
                           match='All arguments are required'):
            credential.Credential.factory(None, 'password')

    def test_creates_credential_instance(self):
        my_credential = credential.Credential.factory(
            'username',
            'password',
        )

        assert isinstance(my_credential, credential.Credential)

    def test_keeps_password_value_when_is_passed(self):
        password = 'password'

        my_credential = credential.Credential.factory(
            'username',
            password,
        )

        assert my_credential.password == password


class TestCredentialProperties:

    def setup(self):
        self.params = {
            "username": "Tserewara",
            "password": "password",
            "active": True
        }

        self.credential = credential.Credential.factory(
            self.params['username'],
            self.params['password'],
            self.params['active'],
        )

    def test_username(self):
        assert self.credential.username == self.params['username']

    def test_password(self):
        assert bool(self.credential.password)

    def test_active(self):
        assert not (self.credential.active is None)


class TestPasswordSetter:

    def test_set_password(self):
        my_credential = credential.Credential.factory(
            'username',
            'password',
        )

        old_pass = my_credential.password
        my_credential.set_password('new_password')

        assert old_pass != my_credential.password


class TestCredentialEquality:

    def test_returns_false_when_username_is_different(self):
        credential_a = credential.Credential.factory(
            'johndoe',
            'password',
        )

        credential_b = credential.Credential.factory(
            'fulano',
            'password',
        )

        assert credential_a != credential_b

    def test_returns_false_when_password_is_different(self):
        credential_a = credential.Credential.factory(
            'johndoe',
            'password1',
        )

        credential_b = credential.Credential.factory(
            'johndoe',
            'password2',
        )

        assert credential_a != credential_b

    def test_returns_true_when_username_and_password_are_equal(self):

        credential_a = credential.Credential.factory(
            'johndoe',
            'password',
        )

        credential_b = credential.Credential.factory(
            'johndoe',
            'password',
        )

        assert credential_a == credential_b


class TestVerifyPassword:

    def test_returns_false_when_password_does_not_match(self):
        my_credential = credential.Credential.factory(
            username='tserewara',
        )

        my_credential.set_password("pass1word")

        assert not my_credential.verify_password('password')

    def test_returns_true_when_password_matches(self):
        password = 'password'
        my_credential = credential.Credential.factory(
            username='tserewara',
        )
        my_credential.set_password(password)

        assert my_credential.verify_password(password)


class TestDeactivate:

    def test_set_active_to_false_when_deactivates(self):
        my_credential = credential.Credential.factory(
            username='tserewara',
            active=True
        )

        my_credential.deactivate()
        assert not my_credential.active
