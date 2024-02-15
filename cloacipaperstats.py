# All data in data.json are N2O fluxes integrated over a time period
# with the trapezodial rule. They are represented as lists of lists,
# [[m_live1, m_live2, ...], [m_control1, m_control2...]], where each
# element (each number) is an integrated time flux (microcrams per
# square meter), and where the first list ("m_live") comes from plots
# treated with digestate with enriched living Cloacibacter sp., while
# the second list ("m_control") comes from soils treated with
# digestate where Cloacibacter sp. was not alive.

# There are three experiments: foursoils (field bucket experiment),
# ninety_days (field bucket experiment) and fieldplot (field plot
# experiment)

# * Imports

import scipy
import numpy as np
from scipy.stats import t as tdist
import json

# * Fieller ratio function

def fieller_confint_mot(x, y, level=.95): # from Intuitive Biostatistics
    """return a fieller confidence interval for x/y. x and y can be unpaired"""
    x = np.array(x)
    y = np.array(y)
    Nx = len(x)
    Ny = len(y)
    SEMx = x.std(ddof=1)/np.sqrt(Nx)
    SEMy = y.std(ddof=1)/np.sqrt(Ny)
    mx = x.mean()
    my = y.mean()
    Q = mx/my
    df = len(x) + len(y) - 2
    tstar = tdist.ppf(1-(1-level)/2, df)
    g = (tstar * SEMy/my)**2
    if (g >= 1):
        error("Quotient not statistically significantly different from zero at the specified level")
    SE_Q = Q/(1-g)*np.sqrt((1 - g)*SEMx**2/mx**2 + SEMy**2/my**2)
    return Q/(1-g) + np.array([-1, 1]) * tstar * SE_Q

# * data

# all data are [cloacilive_fluxes, cloacidead_fluxes] cumulated 90
# days bucket experiment. Fluxes [[live cloaci], [control]] from nine
# periods.

data = json.load(open('data.json'))

ninety_days = data['ninetydays']

foursoils = data['foursoils']

fieldplot = data['fieldplot']

#--

def percent_reduction(fraction_CI):
    """e.g,  turn [.1 .3] into [70, 90] """ 
    return 100 * (1 - np.flip(fraction_CI))

#--

print("\n\n1) Reported results, percent reduction:")

# * 90 days buckets

print("\n\n a) 90 days experiment, 95% confidence intervals by Fieller:")
print("\n")

for period, data in ninety_days.items():
    confint = fieller_confint_mot(*data, 0.95)
    print(period, ':')
    print(percent_reduction(confint[:2]), '\n')
    
# * 4 soils

print("\n b) Four soils experiment, 95% confidence intervals by Fieller:")
print("\n")

for soil in ['calcite', 'organic', 'sand', 'unlimed']:
    CI = fieller_confint_mot(*foursoils[soil], 0.95)
    print('   ', soil, percent_reduction(CI))

# * field plot experiment

print("\n c) Field plot experiment, 95% confidence intervals by ttest on ratios:")

for res in (fieldplot['1'], fieldplot['2']):
    six_ratios_fb = [res[0][i]/res[1][j]
                     for (i, j) in ((0,1), (1,0), (2,3), (3,2), (4,5), (5,4))]

    ttestres = scipy.stats.ttest_1samp(six_ratios_fb, 1)

    confint_fieldplot = ttestres.confidence_interval(confidence_level=0.95)
    low, high = confint_fieldplot.low, confint_fieldplot.high
    print("\n ", percent_reduction([low, high]))

# * simple bootstrap


print("\n\n\n2) Simple bootstrap tests:")



# * bootstrap tests and confidence intervals

# Calculates a bootstrap interval for ratios of means 
def simple_ratio_bootstrap(x, y, N=10000, level=0.95):
    r = []
    for i in range(N):
        xsamp = np.random.choice(x, len(x))
        ysamp = np.random.choice(y, len(y))
        r.append(xsamp.mean()/ysamp.mean())
    r.sort()
    alpha = 1-level
    I1 = int(N*alpha/2)
    I2 = int(N-N*alpha/2)
    return np.array([r[I1], r[I2]])



print("\n a) 90 days experiment, 95% simple bootstrap confidence intervals:")
for period, (x, y) in ninety_days.items():
    bci = simple_ratio_bootstrap(x, y)
    print(" ", percent_reduction(bci))

print("\n b) Four soils experiment, 95% simple bootstrap confidence intervals:")

for soil in ['calcite', 'organic', 'sand', 'unlimed']:
    CI = simple_ratio_bootstrap(*foursoils[soil])
    print('   ', soil, percent_reduction(CI))


print("\n c) Field plot experiment, 95% simple bootstrap confidence intervals (no blocks):")
print(" ", percent_reduction(simple_ratio_bootstrap(*fieldplot['1'])))
print(" ", percent_reduction(simple_ratio_bootstrap(*fieldplot['2'])))

# The last one becomes different from the fieller ratio:
# [-30, 40] insead of [-8, 31]



