import numpy as _np
from os import path


__here__ = path.dirname(__file__)


lr04 = _np.recfromcsv(path.join(__here__, 'lr04.csv'))
