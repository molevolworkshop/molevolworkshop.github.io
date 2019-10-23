#!/usr/bin/env python
import random
from math import log, exp
try:
    from scipy.stats.distributions import beta
    have_beta = True
except:
    have_beta = False

num_heads = 232
num_tails = 261
num_tosses = num_tails + num_heads
num_steps = 100000
prop_width = 0.1

# choose starting parameter value that is good (the MLE, in this case)
theta = num_heads/(float(num_tosses))

# Create 100 bins to store the count of how much of the chain we spend in each interval
num_bins = 100
bin = [0] * num_bins

for i in xrange(num_steps):
    # propose a new theta
    prop_diff = prop_width*(random.random() - 0.5)
    prop_theta = theta + prop_diff

    # reflect theta it is out of bounds (< 0 or > 1)
    if prop_theta < 0.0:
        prop_theta = -prop_theta
    elif prop_theta > 1.0:
        prop_theta = 2 - prop_theta

    # calculate the log of the likelihood ratio
    ln_like_ratio = num_heads*(log(prop_theta) - log(theta)) + num_tails*(log(1 - prop_theta) - log(1 - theta))
    # calculate the log of the prior ratio - uniform prior => prior ratio = 1.0
    ln_prior_ratio = 0.0
    # calculate the log of the Hastings ratio - symmetric proposal => Hastings ratio = 1.0
    ln_hastings_ratio = 0.0

    # calculate the log of the acceptance prob
    ln_acceptance = ln_like_ratio + ln_prior_ratio + ln_hastings_ratio

    if ln_acceptance >= 0.0:
        accept_prob = 1.0
    elif ln_acceptance < -300:
        accept_prob = 0.0
    else:
        accept_prob = exp(ln_acceptance)

    # draw a random number to see if we accept the move
    if random.random() < accept_prob:
        # Accepting! Yay!
        theta = prop_theta
    
    bin[int(theta*num_bins)] += 1

for i, v in enumerate(bin):
    lower_val = i/100.0
    upper_val = (i+1)/100.0
    mcmc_est = v/float(num_steps)
        
    # We can get the exact value by using the fact that:
    #   - if you use a beta(a, b) distribution as your prior (the uniform that we used is a beta(1,1) distribution)
    #   - you use a binomial likelihood function in which you see h heads and t tails 
    #   - the posterior will be a beta(a + h, b + t) distribution
    # See http://en.wikipedia.org/wiki/Conjugate_prior if you are curious
    if have_beta:
        exact = beta.cdf(upper_val, num_heads + 1, num_tails + 1) - beta.cdf(lower_val, num_heads + 1, num_tails + 1)
        print '%.2f - %.2f      %.4f  %.4f' % (lower_val, upper_val, mcmc_est, exact)
    else:
        print '%.2f - %.2f      %.4f' % (lower_val, upper_val, mcmc_est)

