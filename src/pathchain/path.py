# -*- coding: utf-8 -*-
"""
Implementation of the pathlib.Path object

@author: kolja
"""

from pathlib import Path as _Path

class Path(type(_Path())):
    """
    Subclass of pathlib.Path that adds method chaining support.
    Works as a drop-in replacement for pathlib.Path.
    """

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):  # type: ignore
        """Chainable mkdir."""
        super().mkdir(mode=mode, parents=parents, exist_ok=exist_ok)
        return self

    def rmdir(self):  # type: ignore
        """Chainable rmdir."""
        super().rmdir()
        return self

    def chmod(self, mode):  # type: ignore
        """Chainable chmod."""
        super().chmod(mode)
        return self

    def touch(self, mode=0o666, exist_ok=True):  # type: ignore
        """Chainable touch."""
        super().touch(mode=mode, exist_ok=exist_ok)
        return self

    def rename(self, target):  # type: ignore
        """Chainable rename. Returns new Path pointing to target."""
        new_path = super().rename(target)
        return self.__class__(new_path)

    def replace(self, target):  # type: ignore
        """Chainable replace. Returns new Path pointing to target."""
        new_path = super().replace(target)
        return self.__class__(new_path)

    def symlink_to(self, target, target_is_directory=False):  # type: ignore
        """Chainable symlink creation."""
        super().symlink_to(target, target_is_directory=target_is_directory)
        return self

    def hardlink_to(self, target):  # type: ignore
        """Chainable hardlink creation."""
        super().hardlink_to(target)
        return self

    def unlink(self, missing_ok=False):  # type: ignore
        """Chainable unlink."""
        super().unlink(missing_ok=missing_ok)
        return self

    def write_text(self, data, encoding=None, errors=None, newline=None):  # type: ignore
        """Chainable write_text."""
        super().write_text(data, encoding=encoding, errors=errors, newline=newline)
        return self

    def write_bytes(self, data):  # type: ignore
        """Chainable write_bytes."""
        super().write_bytes(data)
        return self

    def assert_exists(self):
        """Chainable assertion that path exists."""
        assert self.exists(), f"{self.resolve()} does not exist"
        return self
