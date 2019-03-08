import numpy as np
import scipy.misc
from scipy.misc import imsave
import os


def save_images(X, save_path):
  # [-1, 1] -> [0,255]
  if isinstance(X.flatten()[0], np.floating):
    # X = ((X + 1.) * 127.5).astype('uint8')
    X = (X * 255).astype('uint8')

  n_samples = X.shape[0]
  rows = int(np.sqrt(n_samples))
  while n_samples % rows != 0:
    rows -= 1

  nh, nw = rows, n_samples // rows

  if X.ndim == 2:
    X = np.reshape(X, (X.shape[0], int(np.sqrt(X.shape[1])), int(np.sqrt(X.shape[1]))))

  if X.ndim == 4:
    h, w = X[0].shape[:2]
    img = np.zeros((h * nh, w * nw, 3))
  elif X.ndim == 3:
    h, w = X[0].shape[:2]
    img = np.zeros((h * nh, w * nw))

  for n, x in enumerate(X):
    j = n // nw
    i = n % nw
    img[j * h:j * h + h, i * w:i * w + w] = x

  imsave(save_path, img)

def mkdir(dir_name):
  if not os.path.exists(dir_name):
    os.makedirs(dir_name)


# nat_grad = np.reshape(np.load('./nat_grad.npy'), [-1, 28, 28])
# adv_grad = np.reshape(np.load('./adv_grad.npy'), [-1, 28, 28])
# natural = np.reshape(np.load('./mnist_X.npy'), [-1, 28, 28])
adv = np.reshape(np.load('./X_adv.npy'), [-1, 28, 28])
# import pdb
# pdb.set_trace()
# for i in range(64):
#   nat_grad[i] = (nat_grad[i] - nat_grad[i].min()) / (nat_grad[i].max()-nat_grad[i].min())
#   adv_grad[i] = (adv_grad[i] - adv_grad[i].min()) / (adv_grad[i].max()-adv_grad[i].min())

# save_images(nat_grad, './nat_grad.png')
# save_images(adv_grad, './adv_grad.png')
# save_images(natural, './natural.png')
save_images(adv, './adv.png')

