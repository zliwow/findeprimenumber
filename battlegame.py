while True:
    # Base stats
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dragon_hp = 300
    dragon_damage = 50
    # Orc stats
    orc = "Orc"
    orc_hp = 200
    orc_damage = 80
    # Place holder for Exit
    exit = "Exit"
    exit_hp = 0
    exit_damage = 0
    # First while loop for character selection
    while True:
        print("1) Wizard", "\n2) Elf", "\n3) Human", "\n4) Orc", "\n5) Exit")
        # .lower() is used to tackle the Bounus Task 2
        character = input("Choose your character: ").lower()
        # The Or oerator is used to tackle the Bounus Task 1
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        # Additional if statement to add Orc
        if character == "4" or character == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        # Terminate for Exit
        if character == "5" or character == "Exit":
            quit()

        else:
            print("Unkown character")

    print("You have choosen: ", character,
          "\nHealth: ", my_hp, "\nDamage: ", my_damage)
    # Second while loop for the battle with dragon
    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damage the Dragon!",
              "\nThe Dragon's hitpoints are now:", dragon_hp, "\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The", character, "took damage!", "\nThe",
              character, "now has", my_hp, "hiitpoints", "\n")
        if my_hp <= 0:
            print("You have lost the battle!")
            break
    while True:
        answer = str(input('Run again? (y/n): ').lower())
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
