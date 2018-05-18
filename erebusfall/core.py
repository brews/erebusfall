import numpy as np
from scipy.interpolate import interp1d
from . import benthic_stacks as stacks


def icevol_correction(age, proxyvalue, proxytype='d18o', timeunit='ya', 
                      benthic_stack=None):
    """Correct isotopic proxy data for ice-volume contribution

    This function uses the LR04 benthic stack scaled such that the LGM-present
    change is assumed to be 1 per mil in accordance with the pore-water 
    estimate of Schrag et al., 1996, Science. Adapted from code written by 
    Jess Tierney.

    Parameters
    ----------
    age: ndarray
        Age array associated with proxy data.
    proxyvalue: ndarray
        Isotopic proxy data to be corrected.
    proxytype: str, optional
        Type of proxy. Must be 'd18o' for δ18O or 'dd' for δD. 
        Default is 'd18o'.
    timeunit: str, optional
        Time unit for 'age'. Must be 'ya' (for years BP), 'ka' 
        (thousand years BP), or 'ma' (million years BP). Default is 'ya'.
    benthic_stack: obj, optional
        Benthic stack to use for ice-volume correction. Uses 
        erebusfall.benthic_stacks.lr04 by default. This is derived from
        DOI: 10.1594/PANGAEA.701576.

    Returns
    -------
    A numpy array giving the corrected isotope data.
    """
    age = np.array(age)
    proxyvalue = np.array(proxyvalue)
    assert len(age) == len(proxyvalue)

    proxytype = proxytype.lower()
    timeunit = timeunit.lower()
    assert proxytype in ['d18o', 'dd']
    assert timeunit in ['ya', 'ka', 'ma']

    if benthic_stack is None:
        benthic_stack = stacks.lr04

    sage = benthic_stack.age.copy()
    if timeunit == 'ya':
        sage *= 1000
    elif timeunit == 'ma':
        sage /= 1000

    # Linearly interpolate the scaled benthic stack to the target data ages.
    interp_f = interp1d(sage, benthic_stack.delo_scaled, kind='linear', 
                        bounds_error=False)
    target = interp_f(age)

    # Find any ages that are negative (e.g., post-1950) and turn to 0
    modern = age < 0
    if any(modern):
        target[modern] = 0

    # Find any ages that are greater than the end of the benthic stack and set
    # then to nan.
    ancient = age > max(sage)
    if any(ancient):
        target[ancient] = np.nan

    # adjust the isotope data
    if proxytype == 'dd':
        target = 8 * target
    corrected = ((1000 + proxyvalue) / (target / 1000 + 1)) - 1000

    return corrected
