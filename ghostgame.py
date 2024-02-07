import random

class Ghost:
    def __init__(self):
        self.energy = 100  # Ghost's energy level

    def scare(self):
        scare_tactics = [
            "Boo! 👻",
            "Eerie moaning fills the air...",
            "Objects begin to float mysteriously...",
            "Glowing eyes appear in the darkness...",
            "The temperature drops suddenly..."
        ]
        scare_tactic = random.choice(scare_tactics)
        print("The ghost tries to scare the visitors:", scare_tactic)

class Visitor:
    def __init__(self, name, fear_tolerance):
        self.name = name
        self.fear_tolerance = fear_tolerance

def main():
    # Initialize ghost
    ghost = Ghost()

    # Initialize visitors
    visitors = [
        Visitor("Tourist", random.randint(50, 70)),
        Visitor("Ghost Hunter", random.randint(60, 80)),
        Visitor("Skeptic", random.randint(40, 60))
    ]

    # Game loop
    while ghost.energy > 0 and any(visitor.fear_tolerance > 0 for visitor in visitors):
        # Player input
        player_action = input("Press 's' to scare visitors, or 'q' to quit: ")

        if player_action == 'q':
            print("Quitting the game.")
            break
        elif player_action == 's':
            # Ghost scares visitors
            ghost.scare()

            # Visitors react to scare tactics
            for visitor in visitors:
                if random.random() < 0.8:  # 80% chance of being scared
                    visitor.fear_tolerance -= random.randint(5, 15)
                    print(f"{visitor.name} is getting scared. Fear tolerance: {visitor.fear_tolerance}")

            # Consume energy
            ghost.energy -= random.randint(5, 15)
            print(f"Ghost's energy level: {ghost.energy}")

    # Game over
    if ghost.energy <= 0:
        print("The ghost has run out of energy. Visitors remain in the haunted house.")
    else:
        print("Congratulations! The ghost has successfully scared away all the visitors.")

if __name__ == "__main__":
    main()

