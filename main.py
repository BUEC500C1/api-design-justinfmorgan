from tweepVisionApi import searchAndAnalyzeImage
import sys

def main():
    #CHECK ARGUMENTS!
    if(len(sys.argv) < 2):
        print("Please provide a search term argument in quotes")
        sys.exit(1)
    else:
        jsonOutput = searchAndAnalyzeImage(sys.argv[1])
        print(jsonOutput)

if __name__ == "__main__":
    main()