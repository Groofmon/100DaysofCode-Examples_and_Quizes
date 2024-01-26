line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

print("Hiding your treasure! X marks the spot.")
place = input()

if place[0] == "A" and place[1] == "1":
    line1[0] = "X"
elif place[0] == "A" and place[1] == "2":
    line2[0] = "X"
elif place[0] == "A" and place[1] == "3":
    line3[0] = "X"

elif place[0] == "B" and place[1] == "1":
    line1[1] = "X"
elif place[0] == "B" and place[1] == "2":
    line2[1] = "X"
elif place[0] == "B" and place[1] == "3":
    line3[1] = "X"

elif place[0] == "C" and place[1] == "1":
    line1[2] = "X"
elif place[0] == "C" and place[1] == "2":
    line2[2] = "X"
elif place[0] == "C" and place[1] == "3":
    line3[2] = "X"

print(f"{line1}\n{line2}\n{line3}")