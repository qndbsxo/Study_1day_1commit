# Installation of NumPy

- If you have Python and PIP already installed on a system, then Installation of NumPy is very easy.
- Install it using this command:

```cmd
pip install numpy
```

If this command falls, then use a python distribution that already has NumPy installed like, Anaconda, Spyder etc.

# Import NumPy

Once NumPy is installed, import it in your application by adding the `import` keyword:

```python
import numpy```

Now Numpy is imported and ready to use.
```python
# Example
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
```

# Numpy as np

- Numpy is usually imported under the np alias.
- alias: In Python alias are an alternate name for referring to the same thing.
- Create an alias with the as keyword while importing:

``` python
import numpy as np
```

Now the Numpy package can be referred to as `np` instead of `numpy`.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

# Checking Numpy Version

The version string is stored under __version__ attribute.

``` python
import numpy as np

print(np.__version__)
```

# REFERENCE

<https://www.w3schools.com/python/numpy/numpy_getting_started.asp>
