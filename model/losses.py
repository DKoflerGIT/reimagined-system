import numpy as np


def root_mean_square(output, target):
    loss = 0.5 * np.sum(np.power(target - output, 2)) # https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
    loss_gradient = output - target
    return loss, loss_gradient

def crossentropy(output, target): # https://towardsdatascience.com/derivative-of-the-softmax-function-and-the-categorical-cross-entropy-loss-ffceefc081d1
    s = output + 1e-6 # log s is undefined if s=0
    loss = - np.sum(target * np.log(s))
    loss_gradient = output - target
    return loss, loss_gradient