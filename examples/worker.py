import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maybe import Just
from mite import Worker


def func_a(x):
    x["a"] = 1
    return x


def func_b(x):
    x["b1"] = 2
    return x


pipeline = lambda x: Just(x).do(func_a).do(func_b)
worker = Worker(pipeline=pipeline)
worker.run()