.. pathchain documentation master file, created by
   sphinx-quickstart on Sun Oct  5 13:08:51 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pathchain - chainable extension of :py:class:`python:pathlib.Path`
==================================================================

During a data science project and building modular functions with the :py:meth:`xarray:xarray.Dataset.pipe` functions
provided by :py:class:`xarray:xarray.Dataset` a subclass of :py:class:`python:pathlib.Path` was written, to make a path pipeline
combining :py:meth:`Path.joinpath` and :py:meth:`Path.mkdir`. Instead of coping this class between project, it is made
available as package on pypi.

A similar approach can be found in :py:class:`ubelt:ubelt.Path` class of the `ubelt <https://pypi.org/project/ubelt/>`_ package, 
although this utility package provides a variety of different extensions to the standart-library, 
and they are subclassing :py:class:`python:str` instead of :py:class:`python:pathlib.Path`.


.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   setup
   package
   changelog
   
You can find more information on
- the `repository <https://github.com/kolja-wagner/pathchain>`_
- the `documentation <https://python-pathchain.readthedocs.io/en/latest/>`_
- the `PyPi page <https://pypi.org/project/pathchain/>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
