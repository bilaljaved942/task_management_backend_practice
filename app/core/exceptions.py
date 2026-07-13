class UserAlreadyExistsError(Exception):
    """Raised when registering with an existing email."""


class InvalidCredentialsError(Exception):
    """Raised when login credentials are invalid."""


class UnauthorizedError(Exception):
    """Raised when a JWT is invalid or missing."""


class TaskNotFoundError(Exception):
    """Raised when a task does not exist."""


class PermissionDeniedError(Exception):
    """Raised when a user accesses another user's resource."""