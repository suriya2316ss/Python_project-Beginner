import random,time
from playsound import playsound

def play(max_tries,top):
    target=random.randint(1,top)
    tries=0
    while tries<max_tries:
        tries+=1
        guess=int(input(f"Attempt{tries}/{max_tries},guess(1-{top}):"))
        if guess==target:
            print("You guess no is correc!")
            playsound(r"Project\Beginner\number_guess\sounds\victory-shouts-demo-310503.mp3")
            return True,tries
        if guess<target:
            print("Too low.")
            playsound(r"Project\Beginner\number_guess\sounds\failure-1-89170.mp3")
        else:
            print("Too high")
            playsound(r"Project\Beginner\number_guess\sounds\fail-trumpet-02-383962.mp3")
    print(f'Out of tries.Number was{target}')
    playsound(r"Project\Beginner\number_guess\sounds\wrong-buzzer-6268.mp3")
    return False,tries

def main():
    print("Number guessing Game:")
    top=int(input("Max number:")or 100)
    tries=int(input("Max attempts:")or 7)
    start=time.time()
    win,used=play(tries,top)
    elapsed=time.time()-start
    print(f"Result:{'win' if win else 'Loss'},attemps used:{used},time:{elapsed:.1f}s")

if __name__=="__main__":
    main()
