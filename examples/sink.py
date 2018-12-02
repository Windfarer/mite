import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maybe import Just, Nothing
from mite import Sink

sink = Sink()

for i in sink:
    if isinstance(i, Nothing):
        print("error", i.err, i.unwrap())
    elif isinstance(i, Just):
        print("result", i.unwrap())
