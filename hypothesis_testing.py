import math
from scipy import stats
from functions import *

def test_for_mean(sample_mean, test, variance, n, confidence, big_sample= True, true_var=True):
    '''Computes whether to accept or reject H0: mean=test'''
    alpha = 1-confidence
    accept = True
    
    #small sampe size with normally distributed r.v. with known true variance
    if not big_sample and true_var:
        quantile = compute_z_statistic(1-alpha/2)
    #small sampe size with normally distributed r.v. with uknown true variance    
    elif not big_sample and not true_var:
        quantile = compute_t_statistic(1-alpha/2, n-1)
    #big sample size with any distribution 
    else:
        quantile = compute_z_statistic(1-alpha/2)
        
    statistic = (sample_mean-test)/math.sqrt(variance/n)
    
    if statistic < -quantile or statistic > quantile:
        accept = False
    
    return accept, quantile, statistic
      

def test_for_variance(sample_variance, n, test, confidence):
    '''Computes whether to accept or reject H: variance = test'''
    alpha = 1-confidence
    accept = True
    
    chi_lower = compute_chi_statistic(alpha/2, n-1)
    chi_upper = compute_chi_statistic(1- alpha/2, n-1)
    
    statistic = sample_variance * (n-1)/test
    
    if statistic<chi_lower or statistic>chi_upper:
        accept = False
    return accept, chi_lower, chi_upper, statistic

def test_for_difference_means(Xmean, Ymean, Xvar, Yvar, Xsize, Ysize, confidence, test):
    '''Computes whether H0: meanX - meanY = test'''
    alpha = 1-confidence
    accept = True
    
    quantile = compute_t_statistic(1-alpha/2, Xsize+Ysize-2)
    
    statistic = (meanX - meanY - test)/math-sqrt((Xsize+Ysize)*((Xsize-1)*Xvar + (Ysize-1)*Yvar)
                                                   /(Xsize*Ysize*(Xsize+Ysize-2)))
    
    if statistic < - quantile or statistic > quantile:
        accept = False
        
    return accept, quantile, statitic    

