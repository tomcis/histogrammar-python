#script to fill histogram using Bin primitive and cms event data

from histogrammar.tutorial import cmsdata
events = cmsdata.EventIterator()

from histogrammar import *

histogram = Bin(100, 0, 100, lambda event: event.met.pt)

for i, event in enumerate(events):
        if i == 1000: 
            break
        histogram.fill(event)

import json
#stores data in json format
testdata = json.dumps(histogram.toJsonFile("test1.json"), indent=4)
print(testdata)
