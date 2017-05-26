# -*- coding: utf-8 -*-


import random
import numpy as np
import matplotlib.pylab as plt

'''
where:
Rate: is the TCP transfer rate or throughputd
MSS: is the maximum segment size (fixed for each Internet path, typically 1460 bytes)
RTT: is the round trip time (as measured by TCP)
p: is the packet loss rate.
'''

Rate = (MSS/RTT) * (1/np.sqrt(p))


def Rate(MSS, RTT, p, w, Q, G, T0, wmax):
    if w(p) < wmax:
        Rate = MSS * (((1-p)/p) + w(p) + Q(p, w(p)) / (1-p))/\
        (RTT * (w(p) + 1) + (Q(p, w(p)) * G(p) * T0) / (1-p))
    else:
        Rate = MSS * (((1 - p) / p) + wmax + Q(p, wmax) / (1 - p)) /\
        (RTT * (0.25 * wmax + ((1 - p) / (p * wmax) + 2)) +
         (Q(p, wmax) * G(p) * T0) / (1 - p))
    return Rate


def w(p):
    return (2 / 3) * (1 + np.sqrt((3 * ((1 - p) / p) + 1)))


def Q(p, w):
    return np.min([1, ((1 - np.power(1 - p, 3)) * (1 + np.power(1 - p, 3)) * (1 - np.power(1 - p, w - 3))) /
                   (1 - np.power(1 - p, w))])

def G(p):
    return np.sum([np.power(2, i - 1) * np.power(p, i) for i in range(6)])


class StateMahcine(object):
    def __init__(self, W_0, C_0, L_0=0, E_0=1, R_0):
        '''
        W_0: transmition windowa
        C_0:
        L_0: lost number
        E_0: timeout exponent
        R_: bool, if retransmition
        '''
        self.state = tuple(W_0, C_0, L_0, E_0, R_0)
    def update():
        