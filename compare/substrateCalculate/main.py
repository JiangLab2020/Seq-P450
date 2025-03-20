import sys

from substrateCalculate.getUploadData import getuserdata
from substrateCalculate.processData import Process, calculationData

if __name__ == "__main__":
    whichDatabase = sys.argv[1]
    userdata = sys.argv[2]
    pairdir = sys.argv[3]
    outputdir = sys.argv[4]
    whichUserData = getuserdata(userdata)
    Ranking = calculationData(whichDatabase, whichUserData)
    print(Ranking)
    Process(Ranking, whichDatabase, pairdir, outputdir)
