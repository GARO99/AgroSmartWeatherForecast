from typing import Any

class NotFoundErrorException(Exception):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(detail)