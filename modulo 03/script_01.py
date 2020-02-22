

local = {"latitude": 100000, "longitude": 200000}


for i in range(0,10):
    print("{1} {0:>20} {latitude} {longitude}".format("100", "10",**local))