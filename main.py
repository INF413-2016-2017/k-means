# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *



data = filesManagment.generate_random_data(50,2)
filesManagment.write_data(data, "out.csv")
p = filesManagment.read_data("out.csv", ignore_first_column=True)

A = alg0(p, 4, 2)
A.run()
display(A.C)

filesManagment.write_solution('sol.csv', C)
