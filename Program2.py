def main():
    
    developerInfo()
    
    score1 = int(input("Enter Score 1: ")) 
    score2 = int(input("Enter Score 2: "))
    score3 = int(input("Enter Score 3: "))
    score4 = int(input("Enter Score 4: "))
    score5 = int(input("Enter Score 5: "))

    avgScore = (score1 + score2 + score3 + score4 + score5)/5

    print("You scored an average of:",avgScore)

    if avgScore > int(70):
        print("You passed, good job!")
    else:
        print("You can do better!") 
  
