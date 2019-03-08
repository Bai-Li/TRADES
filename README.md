# S-O attack for TRADES  

This is the code for Second Order attack (https://arxiv.org/pdf/1901.08573.pdf) for TRADE(https://arxiv.org/pdf/1901.08573.pdf). Currently we only have attacks on MNIST.

## Prerequisites
* Python (3.6.4)
* Pytorch (0.4.1)
* CUDA
* numpy

## Install
We suggest to install the dependencies using Anaconda or Miniconda. Here is an exemplary command:
```
$ wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh
$ bash Anaconda3-5.1.0-Linux-x86_64.sh
$ source ~/.bashrc
$ conda install pytorch=0.4.1
```
#### How to run the attack on MNIST?
* Step 1: Download ```mnist_X.npy``` and ```mnist_Y.npy```.
* Step 2: Run ```pgd_attack_mnist_l2.py```. The adversarial examples will be stored in ```./data_attack```.

In each iteration, it outputs the number of mis-classified examples in each batch and the largest L_2 norm of perturbations.
