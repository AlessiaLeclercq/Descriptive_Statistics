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
