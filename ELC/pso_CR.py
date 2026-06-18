import numpy as np

n_users = 50      # secondary users
n_channels = 60     # available spectrum bands


# Simulate channel gains randomly (in reality this comes from pathloss model)
# SINR[i][j] = signal quality if user i uses channel j
np.random.seed(42)
channel_gain = np.random.uniform(0.1, 1.0, (n_users, n_channels)) # to get SINR which gets throughput
noise = 0.1

print(channel_gain)

SINR = channel_gain / noise  # simplified, no inter-user interference yet

import numpy as np

n = n_channels          # array size
k = 7           # number of ones

arr = np.zeros(n, dtype=int)
arr[np.random.choice(n, k, replace=False)] = 1


# Primary user occupancy: PU[j] = 1 means channel j is occupied by primary user
PU_occupied = arr  # channels 1 and 4 are taken
print(PU_occupied)

def fitness(x):
    channels = np.clip(np.round(x).astype(int), 0, n_channels - 1)
    
    throughput = 0
    penalty = 0
    for user in range(n_users):
        ch = channels[user]
        if PU_occupied[ch]:
            penalty += 1000  # hard penalty for interfering with primary user
        else:
            throughput += np.log2(1 + SINR[user, ch])
    
    # secondary user collision penalty
    for ch in range(n_channels):
        users_on_ch = np.sum(channels == ch)
        if users_on_ch > 1:
            penalty += (users_on_ch - 1) * 1000
    
    return -throughput + penalty


def pso(f, N, S, a, b, b_hat, c, D):

    
    x = np.random.uniform(0, S, size=(N, D))
    v = np.random.normal(size=(N, D))
    p = x.copy()
    p_hat = x[np.argmin(np.apply_along_axis(f, 1, x))]

    for i in range(1000):
        print("doing...",i)
        r, r_hat = np.random.uniform(0, 1, (2, N, D))

        v = a*v + b*r*(p-x) + b_hat*r_hat*(p_hat-x)
        x = x + c*v
        

        for i in range(N):
            if f(x[i]) < f(p[i]):
                p[i] = x[i]
            if f(p[i]) < f(p_hat):
                p_hat = p[i]

    return p_hat


result = pso(
    f=fitness,
    N=300,           # particles
    S=n_channels-1, # search space [0, n_channels-1]
    a=0.7,
    b=1.5,
    b_hat=1.5,
    c=0.1,
    D=n_users       # dimensions = number of users
)


best_assignment = np.clip(np.round(result).astype(int), 0, n_channels-1)

actual_throughput = 0
for user in range(n_users):
    ch = best_assignment[user]
    if not PU_occupied[ch]:
        actual_throughput += np.log2(1 + SINR[user, ch])

print("Channel assignment:", best_assignment)
print("Throughput:", actual_throughput)


