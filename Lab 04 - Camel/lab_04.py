import random

def adventure_game():
    done = False
    gold_collected = 0
    health = 100
    distance_to_destination = 200
    monsters_defeated = 0
    potions_available = 3

    while not done:
        random_distance = random.randint(5, 20)
        random_monster = random.randint(1, 10)
        random_event = random.randint(1, 20)

        print(
            "\nA. Explore.\nB. Rest to restore health.\nC. Drink a health potion.\nD. Check progress.\nQ. Quit."
        )
        choice = input("What is your choice? ").upper()

        if choice == "Q":
            done = True
            print("\nGame Over\n")

        elif choice == "D":
            print(
                f"\nGold collected: {gold_collected}\nHealth: {health}\nDistance to destination: {distance_to_destination}\nMonsters defeated: {monsters_defeated}\nPotions available: {potions_available}\n"
            )

        elif choice == "C":
            if potions_available > 0:
                health += random.randint(15, 30)
                health = min(health, 100)  # Ensure health doesn't exceed 100
                potions_available -= 1
                print("\nYou drank a health potion. Health +{}\n".format(health))
            else:
                print("\nNo potions left!\n")

        elif choice == "B":
            health += random.randint(5, 15)
            health = min(health, 100)  # Ensure health doesn't exceed 100
            print("\nYou rested to restore health. Health +{}\n".format(health))

        elif choice == "A":
            gold_found = random.randint(10, 30)
            gold_collected += gold_found
            distance_to_destination -= random_distance
            health -= random.randint(5, 15)
            monsters_defeated += 1

            if random_event == 1:
                print("\nYou stumbled upon a hidden treasure! +50 gold!\n")
                gold_collected += 50

            elif random_event == 2:
                print("\nYou encountered a fearsome dragon! Health -20!\n")
                health -= 20

            print("\nYou explored and collected {} gold. Distance to destination: {}\n".format(gold_found, distance_to_destination))

        if health <= 0:
            done = True
            print("\nYou were defeated. Game Over!\n")

        if distance_to_destination <= 0:
            done = True
            print("\nCongratulations! You reached your destination!\n")

    print("\nGame Over\n")

