# pathchain – chainable extension of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path)

During a data science project and building modular functions with the 
[`Dataset.pipe`](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.pipe.html) 
methods provided by [`xarray.Dataset`](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.html), 
a subclass of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) was written 
to make a path pipeline combining [`Path.joinpath`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.joinpath) 
and [`Path.mkdir`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir).  

Instead of copying this class between projects, it is made available as a package on PyPI.

A similar approach can be found in the [`ubelt.Path`](https://ubelt.readthedocs.io/en/latest/api/ubelt.Path.html) 
class from the [ubelt](https://pypi.org/project/ubelt/) package, although `ubelt` provides 
a variety of different extensions to the standard library, and subclasses 
[`str`](https://docs.python.org/3/library/stdtypes.html#str) instead of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path).

---

## Install

Install the package using pip:

```bash
pip install pathchain
```

## Develop

- Clone the repository (HTTPS):
```bash
git clone https://github.com/kolja-wagner/pathchain.git
```
- Clone the repository (SSH):
```
git clone git@github.com:kolja-wagner/python-pathchain.git
```
- Install dependencies
```
pip install -e .[dev,doc]
```

## Links

- [PyPI page](https://pypi.org/project/pathchain/)
- [Repository](https://github.com/kolja-wagner/python-pathchain/)
- [Documentation](https://python-pathchain.readthedocs.io/en/latest/)

