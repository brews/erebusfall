import pytest
import numpy as np
import erebusfall

def test_icevol_correction():
    victim = erebusfall.icevol_correction(np.arange(1, 21), [1] * 20, timeunit='ka')
    goal = np.array([ 1.        ,  1.02802878,  0.96636753,  0.96076234,  0.98318348,
                     0.94394714,  0.92152775,  0.89350493,  0.91592306,  0.837464  ,
                     0.79263577,  0.613363  ,  0.53495135,  0.41175789,  0.29419242,
                     0.14867345,  0.07592984, -0.0023976 ,  0.0311698 ,  0.01438582])
    np.testing.assert_allclose(goal, victim, atol=0.01)


def test_icevol_correction_extraheads():
    victim = erebusfall.icevol_correction(np.arange(-5, 21), [1] * 26, timeunit='ka')
    goal = np.array([ 1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
                     1.        ,  1.        ,  1.02802878,  0.96636753,  0.96076234,
                     0.98318348,  0.94394714,  0.92152775,  0.89350493,  0.91592306,
                     0.837464  ,  0.79263577,  0.613363  ,  0.53495135,  0.41175789,
                     0.29419242,  0.14867345,  0.07592984, -0.0023976 ,  0.0311698 ,
                     0.01438582])
    np.testing.assert_allclose(goal, victim, atol=0.01)


def test_icevol_correction_extratails():
    victim = erebusfall.icevol_correction(np.arange(5315, 5325), [1] * 10, timeunit='ka')
    goal = np.array([ 1.21866616,  1.21081495,  1.20296386,  1.1951129 ,  1.18726207,
                     1.17941135,      np.nan,      np.nan,      np.nan,      np.nan])
    np.testing.assert_allclose(goal, victim, atol=0.01)
