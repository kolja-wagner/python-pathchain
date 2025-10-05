# -*- coding: utf-8 -*-

import sys
import pytest
import pathlib
from pathchain import Path


# --- Helpers ------------------------------------------------------------

def assert_chainable(result, obj, cls):
    """
    - For pathchain.Path: returns the same object (self).
    - For pathlib.Path: returns None.
    """
    if cls is Path:
        assert (result) == obj
    else:
        assert result is None

def assert_returns_path(result, expected, cls):
    """
    - For pathchain.Path: returns Path subclass at expected location.
    - For pathlib.Path: returns pathlib.Path at expected location.
    """
    if cls is Path:
        assert isinstance(result, Path)
    else:
        assert isinstance(result, pathlib.Path)
    assert result == expected


def assert_chainable_write(result, obj, cls, expected_len):
    """
    - For pathchain.Path: returns self (chainable)
    - pathlib.Path: returns number of characters/bytes written
    """
    if cls is Path:
        assert isinstance(result, Path)
        assert result == obj
    else:
        assert result == expected_len


@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_mkdir_rmdir(tmp_path, cls):
    p = cls(tmp_path) / "nested"
    assert_chainable(p.mkdir(parents=True), p, cls)
    assert p.exists()
    assert_chainable(p.rmdir(), p, cls)
    assert not p.exists()

@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_touch_unlink(tmp_path, cls):
    p = cls(tmp_path) / "file.txt"

    assert_chainable(p.touch(), p, cls)
    assert p.exists()
    assert_chainable(p.unlink(), p, cls)    
    assert not p.exists()
    
@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_write_text(tmp_path, cls):
    txt_file = cls(tmp_path) / "text.txt"
    content = "hello world"

    result = txt_file.write_text(content)
    assert_chainable_write(result, txt_file, cls, expected_len=len(content))

    assert txt_file.exists()
    assert txt_file.read_text() == content

@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_write_bytes(tmp_path, cls):
    bin_file = cls(tmp_path) / "data.bin"
    data = b"\x00\x01\x02"

    result = bin_file.write_bytes(data)
    assert_chainable_write(result, bin_file, cls, expected_len=len(data))

    assert bin_file.exists()
    assert bin_file.read_bytes() == data

@pytest.mark.parametrize("cls", [pathlib.Path, Path])
@pytest.mark.parametrize("method_name", ["rename", "replace"])
def test_rename_replace(tmp_path, cls, method_name):
    src = cls(tmp_path) / "src.txt"
    target = cls(tmp_path) / "target.txt"
    src.write_text("data")

    if method_name == "replace":
        target.write_text("old")

    result = getattr(src, method_name)(target)
    assert_returns_path(result, target, cls)
    assert target.read_text() == "data"
    

@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_chmod(tmp_path, cls):
    p = cls(tmp_path) / "file.txt"
    p.write_text("data")

    result = p.chmod(0o644)
    assert_chainable(result, p, cls)
    
@pytest.mark.skipif(sys.platform.startswith("win"), reason="Requires symlink privileges on Windows")
@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_symlink(tmp_path, cls):
    target = cls(tmp_path) / "target.txt"
    target.write_text("hello")
    link = cls(tmp_path) / "symlink_link"

    # On Windows, must specify target_is_directory=False for files
    result = link.symlink_to(target, target_is_directory=False) \
        if cls is Path else link.symlink_to(target, target_is_directory=False)

    assert_chainable(result, link, cls)
    assert link.exists()
    assert link.resolve() == target.resolve()


@pytest.mark.parametrize("cls", [pathlib.Path, Path])
def test_hardlink(tmp_path, cls):
    target = cls(tmp_path) / "target.txt"
    target.write_text("hello")
    link = cls(tmp_path) / "hardlink_link"

    result = link.hardlink_to(target)

    assert_chainable(result, link, cls)
    assert link.exists()
    assert link.read_text() == target.read_text()
    
def test_assert_exists_pathchain_only(tmp_path):
    p = Path(tmp_path) / "exists.txt"
    p.touch().assert_exists()  # Should not raise

    q = Path(tmp_path) / "missing.txt"
    with pytest.raises(AssertionError):
        q.assert_exists()
