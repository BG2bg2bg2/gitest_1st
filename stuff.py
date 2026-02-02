# ===============================
# RUBRIC-COMPLIANT GAME SYSTEM
# ===============================

# ---------- DATA SETUP ----------

SET_level = 1
SET_money = 100
SET_souls = 0

SET_attributes = (10, 8, 6, 100)

Inventory = []

SET_store = {
    "Sword": 50,
    "Potion": 10,
    "Charm": 20,
    "Key": 30
}

SET_powerups = []

SET_skills = set()

SET_rank = "Novice"

SET_character = {
    "type": "Unknown",
    "skin": "Unknown",
    "eyes": "Unknown",
    "height": "Unknown",
    "hunter": "Unknown"
}



def tuple_update_stat(attr_tuple, index, change):
    """Returns a new tuple with one stat modified (immutability)."""
    lst = list(attr_tuple)
    lst[index] += change
    return tuple(lst)

def unpack_attributes(attr_tuple):
    """Unpacks attribute tuple."""
    strength, intelligence, speed, health = attr_tuple
    return strength, intelligence, speed, health

def apply_stat_change(attr_tuple, stat_name, amount):
    """Applies stat changes using tuple logic."""
    stat_map = {
        "strength": 0,
        "intelligence": 1,
        "speed": 2,
        "health": 3
    }
    index = stat_map.get(stat_name.lower())
    if index is None:
        return attr_tuple
    return tuple_update_stat(attr_tuple, index, amount)


def compare_skills(player_skills, enemy_skills):
    """Performs real set operations."""
    shared = player_skills.intersection(enemy_skills)
    unique_player = player_skills.difference(enemy_skills)
    combined = player_skills.union(enemy_skills)
    return shared, unique_player, combined



def soul_multiplier(multiplier):
    """Closure that remembers multiplier value."""
    def apply_souls(base_souls):
        return base_souls * multiplier
    return apply_souls

double_souls = soul_multiplier(2)



def combat_system():
    """Encapsulated combat system."""
    combat_log = []

    def log_event(msg):
        combat_log.append(msg)

    def attack(attacker, defender, dmg):
        log_event(f"{attacker} attacked {defender} for {dmg} damage")

    return attack, combat_log



def start_game():
    """Handles character creation."""
    global SET_attributes, SET_rank, SET_character

    print("# Character Creation")

    templates = {
        "human": ((10, 9, 7, 100), "Human Novice"),
        "dog": ((8, 6, 12, 90), "Canine Scout"),
        "goblin": ((12, 6, 8, 85), "Goblin Grunt"),
        "bear": ((15, 5, 5, 130), "Bear Brute"),
    }

    def ask_nonempty(prompt):
        while True:
            v = input(prompt).strip()
            if v:
                return v
            print("Please enter a value (cannot be empty).")

    def ask_integer(prompt, min_value=0):
        while True:
            try:
                n = int(input(prompt))
                if n < min_value:
                    print(f"Enter a number >= {min_value}.")
                    continue
                return n
            except ValueError:
                print("Enter a valid integer.")

    while True:
        print("Choose type: Human, Dog, Goblin, Bear, or CUSTOM")
        key = input("Type: ").strip().lower()
        if key in templates or key == "custom":
            break
        print("Invalid type.")

    if key == "custom":
        custom_name = ask_nonempty("Custom type name: ").title()
        print("Define base stats:")
        s = ask_integer("Strength: ", 0)
        i = ask_integer("Intelligence: ", 0)
        sp = ask_integer("Speed: ", 0)
        h = ask_integer("Health: ", 1)
        SET_attributes = (s, i, sp, h)
        SET_rank = f"{custom_name} Novice"
        char_type = custom_name
    else:
        vals, rank = templates[key]
        SET_attributes = vals
        SET_rank = rank
        char_type = key.title()

    SET_character["type"] = char_type
    SET_character["skin"] = ask_nonempty("Skin/Fur color: ")
    SET_character["eyes"] = ask_nonempty("Eye color: ")
    SET_character["height"] = ask_nonempty("Height: ")
    SET_character["hunter"] = ask_nonempty("Hunter type: ")

    print("Character created successfully.")



def display_stats():
    """Displays player stats."""
    s, i, sp, h = unpack_attributes(SET_attributes)
    print("=================")
    print(f"Level: {SET_level}")
    print(f"Rank: {SET_rank}")
    print(f"Souls: {SET_souls}")
    print(f"Strength: {s}")
    print(f"Intelligence: {i}")
    print(f"Speed: {sp}")
    print(f"Health: {h}")
    print("Skills:", ", ".join(SET_skills) if SET_skills else "None")
    print("=================")



def inventory_menu():
    """Manages inventory."""
    global SET_attributes, SET_souls

    while True:
        print("\n# Inventory Menu")
        print("1. View Inventory")
        print("2. Use Item")
        print("3. Free Soul")
        print("4. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            print(Inventory if Inventory else "Inventory Empty")

        elif choice == "2":
            if not Inventory:
                print("Inventory Empty")
                continue

            for i, it in enumerate(Inventory, 1):
                print(f"{i}. {it}")

            sel = input("Select item: ").strip()
            if not sel:
                continue

            if sel.isdigit():
                item = Inventory[int(sel)-1]
            else:
                item = sel.title()

            if item.lower() == "potion":
                SET_attributes = apply_stat_change(SET_attributes, "health", 20)
                print("Potion used (+20 Health)")
            elif item.lower() == "sword":
                SET_attributes = apply_stat_change(SET_attributes, "strength", 2)
                print("Sword equipped (+2 Strength)")
            else:
                print(f"{item} discarded.")

            if item in Inventory:
                Inventory.remove(item)

        elif choice == "3":
            if SET_souls > 0:
                SET_souls -= 1
                print("Soul freed.")
            else:
                print("No souls.")

        elif choice == "4":
            break


def store_menu():
    """Handles store purchases."""
    global SET_money

    while True:
        print("\n# Store")
        print(f"Money: {SET_money}")
        for item, price in SET_store.items():
            print(f"{item}: {price}")

        choice = input("Buy item or EXIT: ").strip()
        if choice.upper() == "EXIT":
            break

        for key in SET_store:
            if key.lower() == choice.lower():
                price = SET_store[key]
                if price <= SET_money:
                    SET_money -= price
                    Inventory.append(key)
                    SET_store.pop(key)
                    print("Item purchased.")
                else:
                    print("Not enough money.")
                break



def apply_powerups():
    """Applies power-ups."""
    global SET_attributes, SET_powerups
    for pu in SET_powerups:
        SET_attributes = apply_stat_change(
            SET_attributes,
            pu.get("statType", ""),
            pu.get("amount", 0)
        )
    SET_powerups.clear()
    print("Power-ups applied.")



def check_level_up():
    """Handles leveling and skill unlocks."""
    global SET_souls, SET_level

    while SET_souls >= 10:
        SET_souls = double_souls(SET_souls - 10)
        SET_level += 1
        SET_skills.add(f"Skill_L{SET_level}")
        print("Level Up! Skill unlocked.")



def main():
    while True:
        try:
            print("\n=== MAIN MENU ===")
            print("1. Make Character")
            print("2. Store")
            print("3. Inventory")
            print("4. View Stats")
            print("5. Apply Power-Ups")
            print("6. Check Level Up")
            print("7. Exit")

            choice = input("Choice: ").strip()
        except Exception:
            print("Input error.")
            continue

        if choice == "1":
            start_game()
        elif choice == "2":
            store_menu()
        elif choice == "3":
            inventory_menu()
        elif choice == "4":
            display_stats()
        elif choice == "5":
            apply_powerups()
        elif choice == "6":
            check_level_up()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")



while True:
    main()
