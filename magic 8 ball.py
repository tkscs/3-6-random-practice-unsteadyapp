import time
while True:
    ques = input("question? ")
    if(ques == "quit"):
        quit()
    start = time.time()
    input("are you ready for the answer?")
    diffrence = time.time()-start
    if(diffrence>4):
        print("no")
    else:
        print("yes")