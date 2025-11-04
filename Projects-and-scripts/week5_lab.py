# Converted code from WET code to DRY code, using functions (still the same if not more lines of code though... just left elifs..?)

def start_scene():
    print("You are in a dark forest. You see two paths.")
    choice1 = input("Do you go 'left' or 'right'? ")
    if choice1 == 'left':
        left_path_scene()
    elif choice1 == 'right':
        right_path_scene()
    else:
        print("Invalid choice. You are lost.")

def bear_scene(choice2):
    if choice2 == 'tiptoe':
        print("You successfully sneak past the bear. You win!")
    elif choice2 == 'run':
        print("You trip while running and the bear wakes up. You lose.")

def river_scene(choice2):
    if choice2 == 'swim':
        print("You are tired from swimming and rest. You win!")
    elif choice2 == 'follow':
        print("You follow the river bank and find a hidden cave. You win!")
    else:
        print("Invalid choice. You are lost.")


def left_path_scene():
    print("You walk down the left path and find a river.")
    choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
    river_scene(choice2)
    

def right_path_scene():
    print("You walk down the right path and encounter a sleeping bear.")
    choice2 = input("Do you 'tiptoe' past or 'run' away? ")
    bear_scene(choice2)

#start_scene()



# FIXED Code Block
player_score = 0 
def add_points(player_score):
    print(f"[Inside Function] Score is now: {player_score}")
    return (player_score + 10)

# --- Main Program ---
print(f"[Outside] Player score is: {player_score}")
playerscore = add_points(player_score)
print(f"[Outside] Player score is: {player_score}") # Why is it still 0?