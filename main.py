from tweepVisionApi import searchAndAnalyzeImage
import sys

def main():
    #CHECK ARGUMENTS!
    if(len(sys.argv) < 2 or len(sys.argv) > 2):
        print("Please provide a single search term argument in quotes")
        return -1
    else:
        try:
            jsonOutput = searchAndAnalyzeImage(sys.argv[1])
            print(jsonOutput)
            return 0
        except(TypeError):
            print("Please provide a valid argument of type string")
            return -1

if __name__ == "__main__":
    main()