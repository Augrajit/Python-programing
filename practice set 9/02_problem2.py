import random
def game():
    print("You are playing a game")
    score=random.randint(1,80)
    with open ("highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
          highscore=int(highscore)
        else:
            highscore=0   
    print(f"Your score:{score}") 
    if(score>highscore or score==highscore ):
        with open ("highscore.txt","w") as f:
            f.write(str(score))#When to write something it should be in string
    return score
game( )            