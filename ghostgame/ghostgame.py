import random
import pygame

# Initialize pygame
pygame.init()

# Set up music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # Play music in an infinite loop

class Ghost:
    def __init__(self):
        self.energy = 100  # Ghost's energy level

    def scare(self, scare_tactic):
        print(f"The ghost tries to scare the visitors with: {scare_tactic}")

def main():
    # Initialize ghost
    ghost = Ghost()

    # Initialize visitors
    visitors = [
        {"name": "Tourist", "fear_tolerance": random.randint(50, 70)},
        {"name": "Ghost Hunter", "fear_tolerance": random.randint(60, 80)},
        {"name": "Skeptic", "fear_tolerance": random.randint(40, 60)}
    ]

    scare_tactics = [
        "Boo! 👻",
        "Eerie moaning fills the air...",
        "Objects begin to float mysteriously...",
        "Glowing eyes appear in the darkness...",
        "The temperature drops suddenly..."
    ]

    # Game loop
    while ghost.energy > 0 and any(visitor["fear_tolerance"] > 0 for visitor in visitors):
        # Player input to choose scare tactic
        print("\nChoose a scare tactic:")
        for i, tactic in enumerate(scare_tactics, 1):
            print(f"{i}. {tactic}")
        print("0. Quit game")
        choice = input("Enter the number of the scare tactic you want to use: ")

        # Check player's choice
        if choice == '0':
            print("Exiting the game...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(scare_tactics):
            # Scare visitors with the chosen tactic
            ghost.scare(scare_tactics[int(choice) - 1])

            # Visitors react to scare tactics
            for visitor in visitors:
                if random.random() < 0.8:  # 80% chance of being scared
                    visitor["fear_tolerance"] -= random.randint(5, 15)
                    print(f"{visitor['name']} is getting scared. Fear tolerance: {visitor['fear_tolerance']}")
                    
                    # Handle visitors whose fear tolerance drops below zero
                    if visitor["fear_tolerance"] <= 0:
                        print(f"{visitor['name']} runs away or dies from fear!")
                        visitors.remove(visitor)

            # Consume energy
            ghost.energy -= random.randint(5, 15)
            print(f"Ghost's energy level: {ghost.energy}")
        else:
            print("Invalid choice. Please choose a valid scare tactic.")

    # Game over
    if ghost.energy <= 0:
        print("The ghost has run out of energy. Visitors remain in the haunted house.")
    else:
        print("Congratulations! The ghost has successfully scared away all the visitors.")

    # Quit pygame
    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()

