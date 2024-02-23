import random

monthly_volume = [
    # [0] -> Name   ,  [1] -> Description   ,  [2] -> Monthly Search Volume as Int
    ["Mexico", "The country of north America", 2_240_000],
    ["Michael Jackson", "The World Star Singer", 4_900_000],
    ["Ups", "The Mega deliver company", 6_120_000],
    ["YouTube", "The most famous video player website", 1_680_000_000],
    ["Adele", "The famous singer", 2_725_000],
    ["Yao Ming", "The Basketball player", 246_000],
    ["Puberty", "The most stressful era for a young", 135_000],
    ["Harassment", "The unwanted sexual approaching", 248_000],
    ["Wonder Woman", "The woman superhero", 7_480_000],
    ["Solar System", "The Star system where we live", 823_000],
    ["Silicon Valley", "The place of all mega companies", 858_000],
    ["Power Rangers", "The superhero team", 4_270_000],
    ["Russia", "The one of the most developed country", 2_240_000],
    ["Dubai", "The fancy arabian city", 2_740_000]

]

compared_list = []
point = 0
choice = ""
result = ""


# START
print("WELCOME TO THE HIGHER/LOWER GAME!")
# defining section a
section_a = monthly_volume[random.randint(0, len(monthly_volume) - 1)]
if section_a not in compared_list:
    compared_list.append(section_a)
section_b = section_a
while True:
    section_a = section_b

    if not len(compared_list) == len(monthly_volume):

        print(
            f" compare 🅰: {section_a[0]} {section_a[1]} has been searched for {section_a[2]} times for previous month")

        # defining section b
        while True:
            section_b = monthly_volume[random.randint(0, len(monthly_volume) - 1)]
            if section_b not in compared_list and section_b != section_a:
                compared_list.append(section_b)
                break

        print(f" with 🅱: {section_b[0]} {section_b[1]}")

        # Making a choice if it's lower or higher
        choice = input("Make your choice(higher or lower): ").lower().strip()

        if section_b[2] > section_a[2]:
            result = "higher"
        elif section_b[2] < section_a[2]:
            result = "lower"

        if choice == result or choice == "g":
            point += 1
            print(f"✅✅✅✅Well Done! {section_b[0]} has been searched for {section_b[2]}")
            print(f"Your point: {point}")
        else:
            print(f"❌❌❌❌You have guessed wrong! {section_b[0]} has been searched for {section_b[2]}")
            print(f"Your point {point}")
            break

    else:
        print(f"You Won! Your point is {point} which is the best score a player is able to get.")
        break
