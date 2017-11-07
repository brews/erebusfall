import numpy as np
from scipy.io import loadmat
from scipy.interpolate import interp1d


def icevolcorr(age, proxydata, proxytype='d18o', timeunit='ya'):
    """Correct isotopic proxy data for ice volume contribution

    This function uses the LR04 benthic stack scaled such that the LGM-present 
    change is assumed to be 1 per mil in accordance with the pore water 
    estimate of Schrag et al., 1996, Science. Adapted from Jess Tierney's 
    original MATLAB function.

    Parameters
    ----------
    age: listlike
        Age array associated with proxy data.
    proxydata: listlike
        Isotopic proxy data to be corrected.
    proxytype: str
        Type of proxy. Must be 'd18o' for δ18O or 'dd' for δD. 
        Default is 'd18o'.
    timeunit: str
        Time unit for 'age'. Must be 'ya' (for years BP), 'ka' 
        (thousand years BP), or 'ma' (million years BP). Default is 'ya'.

    Returns
    -------
    A numpy array giving the corrected isotope data.
    """
    assert len(age) == len(proxydata)
    age = np.array(age)
    proxydata = np.array(proxydata)

    assert proxytype in ['d18o', 'dd']

    assert timeunit in ['ya', 'ka', 'ma']

    lr04 = loadmat('lr04.mat')

    sage = lr04['delob_age'].flatten()
    if timeunit == 'ya':
        sage *= 1000
    elif timeunit == 'ma':
        sage /= 1000

    # linearly interpolate the scaled benthic stack to the target data ages.
    interp_f = interp1d(sage, lr04['deloscaled'].flatten(), kind='linear', bounds_error=False)
    target = interp_f(age)

    # find any ages that are negative (e.g., post-1950) and turn to 0
    modern = age < 0
    if any(modern):
        target[modern] = 0

    # find any ages that are greater than the end of the benthic stack and set
    # then to NaNs.
    ancient = age > max(sage)
    if any(ancient):
        target[ancient] = np.nan

    # correct the isotope data
    if proxytype == 'dd':
        target = 8 * target
    corrected = ((1000 + proxydata) / (target / 1000 + 1)) - 1000

    return corrected
    