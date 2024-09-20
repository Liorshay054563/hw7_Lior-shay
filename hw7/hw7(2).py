# start


high: str = None
score: float = float(input(' what is the score:'))
sum_score: int = 0
counter: int = 0
for i in range(1, 7):
    while score < 5.8:
        print("too low")
        score: float = float(input(' what is the score:'))
    if 5.8 <= score < 6.23:
        print("good score")
        score: float = float(input(' what is the score:'))
        counter += 1
        sum_score += score
    else:
        high: str = input("what is the name of the jumper")
        score: float = float(input(' what is the score:'))
        counter += 1
        sum_score += score

avg: float = sum_score / counter
print(f"{counter} good result, the average is {avg} and the higher belong to {high}")

# end
