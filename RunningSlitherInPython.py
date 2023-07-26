from slither.slither import Slither
from slither.detectors import all_detectors

ListOfContracts = #Add list of smart contracts' source codes here
f = open('sample1.sol', "w+") #Slither requires file format

vulnList = []

# SPEED: 5000 PER SECOND
for i in ListOfContracts:
    f.seek(0)
    f.truncate(0)
    f.seek(0)
    f.write(str(i)) 
    f.flush()
    curContract = Slither("sample1.sol")
    for i in [getattr(all_detectors, name) for name in dir(all_detectors)][:88]:
        try:
            curContract.register_detector(i)
        except:
            print(f"{i} is already in object")
    results = curContract.run_detectors()
    vnrble=[]
    for i in range(0,len(curContract.detectors)):
        curTest = curContract.detectors[i]
        if len(results[i])>0:
            vnrble.append(str(curTest).split(".")[-1].split(" ")[0])
    vulnList.append(vnrble)

# Now handle adding vulnList however you want to whatever you're using