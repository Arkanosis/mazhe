#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

from phystricksMaxVraissLp import MaxVraissLp
from phystricksBiaisOuPas import BiaisOuPas

def AllFigures():
    test_list=[MaxVraissLp,BiaisOuPas]

    tests=main.FigureGenerationSuite(test_list,first=0,title=u"Modélisation")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        pass
