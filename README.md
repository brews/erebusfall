# erebus

[![Travis-CI Build Status](https://travis-ci.org/brews/erebus.svg?branch=master)](https://travis-ci.org/brews/erebus)

Ice-volume correction to marine-isotope 
[δ18O](https://en.wikipedia.org/wiki/%CE%9418O) and [δD](https://en.wikipedia.org/wiki/Deuterium)
 proxy records, in Python.

`erebus` is a simple package for demonstrating how to apply an 
ice-volume correction to a proxy record. The package uses the [LR04 benthic](https://doi.org/10.1594/PANGAEA.701576) 
stack. The stack is scaled so that the [LGM](https://en.wikipedia.org/wiki/Last_Glacial_Maximum)-to-present 
change is assumed to be 1 ‰ in accordance with the pore-water estimate of 
[Schrag et al. 1996](https://doi.org/10.1126/science.272.5270.1930). The 
package is adapted from code originally written by Jess Tierney.


## Example

Start by importing `erebus`, `numpy`:

```python
import erebus
import numpy as np
```

...and creating a hypothetical proxy time 
series...

```python
age_ka = np.arange(0, 20, 1)
proxy = np.random.normal(loc=-2.0, size=len(age_kya))
```

Now we can plug this into `erebus.icevol_correction()` with a few key options:

```python
proxy_adjusted = erebus.icevol_correction(age_ka, proxy, 
                                          proxytype='d18o', 
                                          timeunit='ka')
```

We first plug in the proxy age and proxy values. The `proxytype='d18o'` 
indicates that we're dealing with δ18O. We can set `proxytype='dd'` for a δD 
record. The `timeunit` argument indicates that `age_kya` is in thousands of 
years before present. There are also options for for "years BP" and 
"million years BP". The output from the function, `proxy_adjusted`, is the 
corrected isotope proxy as a numpy array.

See `help(erebus.icevol_correction)` for more documentation.

## Installation

You can install the package [from PyPI](https://pypi.python.org/pypi/erebus) with

```
pip install erebus
```

If you want to use `conda`:

```
conda install erebus -c sbmalev
```

## Development and Support

Source code is [hosted online](https://github.com/brews/erebus) under an Open 
Source license. Please feel free to file any 
[bugs and issues](https://github.com/brews/erebus/issues) you find.
