#bop it limited rounds
#flick it, spin it, twist it,bop it,pull it
import time
import random
import inputimeout   #not a built-in module

def game():
    score=0
    while True:
        round=1
        interval=2          #starting interval
        print('round ',round)
        time.sleep(0.75)    #all these 0.75 pause are just for the game effect,ie dialogue appearing
        while True:
            time.sleep(interval)    #don't really need this but builds the pace of the game by making the dialogues come faster
            if score>=round*4:      #score to score for each round, default is 4
                round+=1
                if round==8:        #last round is 7 in this case
                    print('final score is  ',score)
                    print('you completed the whole game congrats!!!')
                    quit()
                print('round ',round)
                time.sleep(0.75)
                interval-=0.25      #interval lessens with each new round, default is -0.25
            q=random.randint(1,5)   #5 cases
            match q:

                case 1:
                    print('bop it',end='  ')
                    print('press "b"')
                    try:
                        ans=inputimeout.inputimeout(prompt='enter the letter        ',timeout=interval)
                    except Exception:
                        print('timeout game over ', 'final score is ',score)
                        quit()
                    else:
                        if ans=='b':
                            score+=1
                            continue
                        else:
                            print('oops wrong letter')
                            print('timeout game over', 'final score is ',score)
                            quit()                
                case 2:
                    print('pull it',end='  ')
                    print('press "p"')
                    try:
                        ans=inputimeout.inputimeout(prompt='enter the letter        ',timeout=interval)
                    except Exception:
                        print('timeout game over', 'final score is ',score)
                        quit()
                    else:
                        if ans=='p':
                            score+=1
                            continue
                        else:
                            print('oops wrong letter')
                            print('timeout game over', 'final score is ',score)
                            quit()                
                case 3:
                    print('twist it',end='  ')
                    print('press "t"')
                    try:
                        ans=inputimeout.inputimeout(prompt='enter the letter        ',timeout=interval)
                    except Exception:
                        print('timeout game over', 'final score is ',score)
                        quit()
                    else:
                        if ans=='t':
                            score+=1
                            continue
                        else:
                            print('oops wrong letter')
                            print('timeout game over', 'final score is ',score)
                            quit()                
                case 4:
                    print('spin it',end='  ')
                    print('press "s"')
                    try:
                        ans=inputimeout.inputimeout(prompt='enter the letter        ',timeout=interval)
                    except Exception:
                        print('timeout game over', 'final score is ',score)
                        quit()
                    else:
                        if ans=='s':
                            score+=1
                            continue
                        else:
                            print('oops wrong letter')
                            print('timeout game over', 'final score is ',score)
                            quit()                
                case 5:
                    print('flick it',end='  ')
                    print('press "f"')
                    try:
                        ans=inputimeout.inputimeout(prompt='enter the letter        ',timeout=interval)
                    except Exception:
                        print('timeout game over', 'final score is ',score)
                        quit()
                    else:
                        if ans=='f':
                            score+=1
                            continue
                        else:
                            print('oops wrong letter')
                            print('timeout game over', 'final score is ',score)
                            quit()                
            break
        break

start=input('start the game?  y/n  ')
if start=='y':
    time.sleep(0.75)
    print('press the first letter of the word that comes up ')
    game()
else:
    print('young man')
    time.sleep(2)
    print('kill yourself')