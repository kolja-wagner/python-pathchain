# -*- coding: utf-8 -*-
"""
Implementation of the pathlib.Path object

@author: kolja
"""

from pathlib import Path as _Path
from typing import Callable

class Path(type(_Path())):
    """
    Subclass of :py:class:`python:pathlib.Path` that adds method chaining support.
    Can be used as a drop-in replacement 
    """

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):  # type: ignore
        """
        Create a new directory at this path and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.mkdir`.
        """
        super().mkdir(mode=mode, parents=parents, exist_ok=exist_ok)
        return self

    def rmdir(self):  # type: ignore
        """
        Remove this directory and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.rmdir`.
        """
        super().rmdir()
        return self

    def chmod(self, mode):  # type: ignore
        """
        Change the mode of this path and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.chmod`.
        """
        super().chmod(mode)
        return self

    def touch(self, mode=0o666, exist_ok=True):  # type: ignore
        """
        Create a new file at this path (if it does not exist) and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.touch`.
        """
        super().touch(mode=mode, exist_ok=exist_ok)
        return self

    def rename(self, target):  # type: ignore
        """
        Rename this path to the given target and return a new Path instance.
        Wraps :py:meth:`python:pathlib.Path.rename`.
        """
        new_path = super().rename(target)
        return self.__class__(new_path)

    def replace(self, target):  # type: ignore
        """
        Rename this path to the given target, overwriting if necessary, and return a new Path instance.
        Wraps :py:meth:`python:pathlib.Path.replace`.
        """
        new_path = super().replace(target)
        return self.__class__(new_path)

    def symlink_to(self, target, target_is_directory=False):  # type: ignore
        """
        Create a symbolic link pointing to the target and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.symlink_to`.
        """
        super().symlink_to(target, target_is_directory=target_is_directory)
        return self

    def hardlink_to(self, target):  # type: ignore
        """
        Create a hard link pointing to the target and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.hardlink_to`.
        """
        super().hardlink_to(target)
        return self

    def unlink(self, missing_ok=False):  # type: ignore
        """
        Remove this file or symbolic link and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.unlink`.
        """
        super().unlink(missing_ok=missing_ok)
        return self

    def write_text(self, data, encoding=None, errors=None, newline=None):  # type: ignore
        """
        Write string data to this file and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.write_text`.
        
        .. warning::
           Unlike :py:meth:`python:pathlib.Path.write_text`, this method **does not return the number of characters written**. It returns **self** to support method chaining.
        """
        super().write_text(data, encoding=encoding, errors=errors, newline=newline)
        return self

    def write_bytes(self, data):  # type: ignore
        """
        Write bytes to this file and return self for chaining.
        Wraps :py:meth:`python:pathlib.Path.write_bytes`.

        .. warning::
           Unlike :py:meth:`python:pathlib.Path.write_bytes`, this method **does not return the number of characters written**. It returns **self** to support method chaining.
        """
        super().write_bytes(data)
        return self

    def assert_exists(self):
        """
        Assert that this path exists and return self for chaining.

        :return: self
        :raises AssertionError: if the path does not exist
        """
        assert self.exists(), f"{self.resolve()} does not exist"
        return self

    def pipe(self, func: Callable, *args, **kwargs):
        """
        Apply a function to this Path object and return the result.
        This method enables a functional programming style similar to pandas DataFrame.pipe(),
        allowing you to chain operations on Path objects by passing them through custom functions.
        
        :param func: A callable that accepts this Path object as its first argument
        :param args: Positional arguments to pass to func after the Path object
        :param kwargs: Keyword arguments to pass to func
        :return: The result of applying func to this Path object
        """
        return func(self, *args, **kwargs)
    
    def sglob(self, pattern: str, *, case_sensitive=None, recurse_symlinks=False):
        """ An addition to self.glob, that returns a sorted list of the glob results.
        For documentation see :py:meth:`python:pathlib.Path.glob`.
        """
        return sorted(self.glob(pattern, case_sensitive=case_sensitive, recurse_symlinks=recurse_symlinks))
    
