# start

positive: int = None
negative: int = None
div_7: int = 0
num_0: int = 0
x: int = int(input("Enter number between -1000 to 1000:"))
for i in range(1, 5 + 1):  # שינתי ל5 במקום 10 בכדי להקל על הבדיקה

    if x == -9999:
        break   # i cant do the break without printing  "?"
    while -1000 > x or 1000 < x:
        x: int = int(input("Enter number between -1000 to 1000:"))
        print("no")
        continue
    if -1000 < x or 1000 > x:
        print("the number is ok")
        x: int = int(input("Enter number between -1000 to 1000:"))
        if x > 0:
            positive = x
        if x < 0:
            negative = x
        if x == 0:  # this "if" not counting correctly "?"
            num_0 += 1
        if x % 7 == 0:
            div_7 += 1
print(f"positive number {positive} and the negative {negative}, number 0- {num_0}, div in 7- {div_7}")

# end
