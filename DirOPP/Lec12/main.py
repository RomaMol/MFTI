#!/usr/bin/python
# -*- coding: utf-8 -*-
#   https://www.youtube.com/watch?v=KlW6O-5pcuU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=12
#   ООП Python 3 #12: нейронная сеть (пример реализации)
from Lec12.network import NetWork

net = NetWork(10, 5, 3)
net.run([1, 0.5, 0.1, 0.2, 0.7, 0.9, 1, 0.6, 0.3, 0.1])
out = net.output()
print(out)
