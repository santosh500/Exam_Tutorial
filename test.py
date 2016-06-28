import csv

with open("cool.csv", "r") as scoreFile:
    scoreFileReader = csv.reader(scoreFile)
    scoreList = []
    for row in scoreFileReader:
        if len (row) != 0:
            scoreList = scoreList + [row]

scoreFile.close()

print(scoreList)

with open("cool.csv","r") as scoreFile:
          city = input("Enter City: ")
          scoreFileReader = csv.reader(scoreFile)
          for row in scoreFileReader:
              for field in row:
                  if field == city:
                      print(row)

scoreFile.close()
