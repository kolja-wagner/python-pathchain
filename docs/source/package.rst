Package
=======

the contents of the :mod:`pathchain` package.


Concept
-------

A dropin replacement of :py:class:`python:pathlib.Path` to be chained together.
Inspired by the :py:meth:`xarray:xarray.Dataset.pipe` mechanism.

Example ::

    from pathchain import Path
    
    path_file = Path.home()\
                .joinpath("test")\
                .mkdir(exist_ok)\
                .touch()
    
    
Reference
---------

.. autoclass:: pathchain.Path
   :members:
   :member-order: bysource
