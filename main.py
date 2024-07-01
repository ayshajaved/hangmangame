#The hang man game


tup1 = ["p", "y", "t", "h", "o", "n"]
tup2 = ["_", "_", "_", "_", "_", "_"]
x = True

print("The player 1 has decided the word, now it is your turn to guess the word!")
# print(tup2[0], tup2[1], tup2[2], tup2[3], tup2[4], tup2[5])                      #instead i can write it in a more readable form
print(" ".join(tup2))

while x:
    ch = input("enter the character: ")
    if ch in tup1:
        print("YOU GUESSES RIGHT!")
        for i in range(len(tup1)):
            if ch == tup1[i]:
                tup2[i]= ch
                # for i in tup2:
                #     print( i , end = "")
                # print("")                                                         #instead of this for i can simply write the print statement
                print(" ".join(tup2))
                print("")
    else:
        print("WRONG GUESS!TRY AGAIN\n")
    if "_" not in tup2:
        print("THE WORD IS COMPLETED!")
        x = False
