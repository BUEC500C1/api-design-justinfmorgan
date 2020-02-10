from tweepVisionApi import visionAnalysis
#, searchTwitter, searchAndAnalyzeImage
from main import main

def test_apiUnitTest():
    assert visionAnalysis("BADFILE") == -1
    #assert searchTwitter(1124871874501958198590218) == -1
    #assert searchAndAnalyzeImage("129r01*U)FWEJF)*EWJF") == -1
    assert main() == -1 #Test to make sure when no arguments an error occurs
