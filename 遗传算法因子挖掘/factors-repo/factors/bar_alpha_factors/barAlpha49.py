# encoding: UTF-8
# fields = ['open','high','low','close','turnover','volume','openInterest']
import pandas as pd
#from ctaFunction import *

#---------------------------------------------------------------
def barAlpha49(bars,fast=False):
    """Alpha49 of 101 Alphas"""
    close = bars['close']
    inner = (((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10))
    alpha = (-1 * delta(close))
    alpha[inner < -0.1] = 1
    return alpha

