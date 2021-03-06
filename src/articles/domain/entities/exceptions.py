class ArticleNotFound(Exception):
    pass


class CategoryNotFound(Exception):
    pass


class TagNotFound(Exception):
    pass


class DuplicateTag(Exception):
    pass


class DuplicateTitle(Exception):
    pass


class CredentialValueError(Exception):
    pass


class EncryptorTypeError(Exception):
    pass


class PasswordStrengthError(Exception):
    pass
