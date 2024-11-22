with open("example1.txt", "r") as usr_input:
    text = usr_input.read()

digits = []
ans = 0
for line in text.split("\n"):
    for char in line:
        if char.isdigit() == True:
            digits.append(char)
score = int(digits[0] * 10 + digits[-1])
ans += score

print(ans)



