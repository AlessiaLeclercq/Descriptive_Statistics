import math
from scipy import stats

def sample_mean(sample, n):
    return sum(sample)/n

def sample_variance(sample, mean, n):
    return [(s - mean)**2 for s in sample]/(n-1)
    
def compute_t_statistic(param, df):
    return stats.t.ppf(param, df)

def compute_z_statistic(param):
    return stats.norm.ppf(param)

def compute_chi_statistic(param, df):
    return stats.chi2.ppf(param, df)

def confidence_for_mean(sample_mean, variance, n, confidence, big_sample = True, true_var = True):
    '''Computes the two sided confidence intervals for the mean '''

    alpha = 1-confidence
    
    #small sample size with normally distributed r.v. and known true variance
    if not big_sample and true_var:
        quantile = compute_z_statistic(1-alpha/2)
    #small sample size with normally distributed r.v. and unkown true variance
    elif not big_sample and not true_var:
        quantile = compute_t_statistic(1-alpha/2, n-1)
    #Large sample size with wny r.v. distribution and variance
    else:
        quantile = compute_z_statistic(1-alpha/2)
        
    lower = sample_mean - quantile*math.sqrt(variance/n)
    upper = sample_mean + quantile*math.sqrt(variance/n)
    return lower, upper, quantile


def confidence_for_variance(sample_variance, n, confidence):
    '''Computes the confidence interval for the variance of a normally distributed r.v.'''
    alpha = 1-confidence
    chi_lower = compute_chi_statistic(1-alpha/2, n-1)
    chi_upper = compute_chi_statistic(alpha/2, n-1)
    
    lower = sample_variance*(n-1)/chi_lower
    upper = sample_variance*(n-1)/chi_upper
    return lower, upper, chi_lower, chi_upper


def confidence_for_difference_means(Xmean, Ymean, Xvar, Yvar, nx, ny, confidence):
    '''Computes the confidence interval for the difference of the mean of two normally distributed r.v.s'''
    alpha = 1-confidence
    quantile = compute_t_statistic(1-alpha/2, nx+ny-1)
    
    lower = (Xmean - Ymean) - quantile*math.sqrt(Xvar/nx + Yvar/ny)
    upper = (Xmean - Ymean) + quantile*math.sqrt(Xvar/nx + Yvar/ny)
    
    return lower, upper, quantile


def confidence_for_bernoulli(p_est, n, confidence):
    '''Computes the confidence interval for the parameter of a Bernoulli distributed sample'''
    alpha = 1-confidence
    quantile = compute_z_statistic(1-alpha/2)
    
    lower = p_est - quantile * math.sqrt(p_est*(1-p_est)/n)
    upper = p_est + quantile * math.sqrt(p_est*(1-p_est)/n)
    return lower, upper, quantile

def confidence_for_exponential(sample, n, confidence):
    '''Computes the confidence interval for the lambda value of an Exponentially distributed sample'''
    alpha = 1-confidence
    chi_lower = compute_chi_statistic(alpha/2, 2*n)
    chi_upper = compute_chi_statistic(1-alpha/2, 2*n)
    
    lower = chi_lower/(2*sum(sample))
    upper = chi_upper/(2*sum(sample))
    return lower, upper, chi_lower, chi_upper


def prediction_interval(sample_mean, variance, n, confidence, big_sample = True, true_var = True):
    '''Computes the prediction interval for a new observation'''
    alpha = 1-confidence
    
    #small sample size with normally distributed r.v. and known true variance
    if not big_sample and true_var:
        quantile = compute_z_statistic(1-alpha/2)
    #small sample size with normally distributed r.v. and unknown true variance
    elif not big_sample and not true_var:
        quantile = compute_t_statistic(alpha/2, n-1)
    #large sample size with any r.v. distribution
    else:
        quantile = compute_z_statistic(1-alpha/2)
        
    lower = sample_mean - quantile*math.sqrt(variance + variance/n)
    upper = sample_mean + quantile*math.sqrt(variance + variance/n)
    return lower, upper, quantile
