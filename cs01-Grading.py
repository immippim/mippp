WorkScores = int(input("enter your work scores :"))
MidtermScores = int(input("Enter your midterm scores :"))
FinalScores = WorkScores + MidtermScores + FinalScores
if TotalScores >= 80:
    print("A")
elif TotalScores >= 75:
    print("B+")
elif TotalScores >= 70:
    print("B")
elif TotalScores >=65:
    print("C+")
elif TotalScores >=60 :
    print("C")
elif TotalScores >=55 :
    print("D+")
elif TotalScores >=50 :
    print("D")
else :
    print("F")