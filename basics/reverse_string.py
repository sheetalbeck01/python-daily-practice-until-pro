# --------------------------
# Reverse String Using Loops

text = "Delhi"

reversed = ""

for t in text:
    reversed = t + reversed

print(reversed)


# ---------------------------
# Loop backward using indexes

text2 = "Mumbai"

reversed_text2 = ""

for i in range(len(text2) -1,-1,-1):
    reversed_text2 += text2[i]

print(reversed_text2)

# ---------------------------
# Reverse String Using While Loop

text3 = "Ranchi"

length = len(text3)
i = 0
reversed_text3 = ""

while i < length:
    reversed_text3 = text3[i] + reversed_text3
    i += 1

print(reversed_text3)