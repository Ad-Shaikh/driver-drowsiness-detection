import numpy as np


def lip_distance(shape):
    # numpy.concatenate
    # https: // numpy.org/doc/stable/reference/generated/numpy.concatenate.html?highlight = concatenate
    top_lip = shape[50:53]
    top_lip = np.concatenate((top_lip, shape[61:64]))

    low_lip = shape[56:59]
    low_lip = np.concatenate((low_lip, shape[65:68]))

    # https://numpy.org/doc/stable/reference/generated/numpy.mean.html?highlight=mean#numpy.mean
    top_mean = np.mean(top_lip, axis=0)
    low_mean = np.mean(low_lip, axis=0)

    distance = abs(top_mean[1] - low_mean[1])
    return distance
