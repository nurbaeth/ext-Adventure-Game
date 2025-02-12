class Room:
    def __init__(self, name, description, items=None, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __str__(self):
        return f"{self.name}\n{self.description}"

class Game:
    def __init__(self):
        # Создаем комнаты
        self.rooms = self.create_rooms()
        self.current_room = self.rooms['entrance']
        self.inventory = []

    def create_rooms(self):
        entrance = Room("Entrance", "You are at the entrance of a dark dungeon. There's a door to the north.", items=["key"])
        hallway = Room("Hallway", "A narrow hallway, dimly lit. There are doors to the north and south.")
        treasure_room = Room("Treasure Room", "You found the treasure room! A chest sits in the center.", items=["treasure"])
        exit_room = Room("Exit", "You are at the exit. You have escaped the dungeon!")
        
        entrance.north = hallway
        hallway.south = entrance
        hallway.north = treasure_room
        treasure_room.south = hallway
        treasure_room.east = exit_room
        exit_room.west = treasure_room
        
        return {
            'entrance': entrance,
            'hallway': hallway,
            'treasure_room': treasure_room,
            'exit': exit_room
        }

    def start(self):
        print("Welcome to the Dungeon Adventure Game!\n")
        while True:
            print("\nCurrent Room:")
            print(self.current_room)
            
            # Печатаем предметы в комнате
            if self.current_room.items:
                print(f"Items here: {', '.join(self.current_room.items)}")

            command = input("\nWhat do you want to do? (type 'help' for options): ").lower()

            if command == 'quit':
                print("Thanks for playing!")
                break
            elif command == 'help':
                print("Commands: 'go [direction]', 'take [item]', 'inventory', 'quit'")
            elif command.startswith("go "):
                self.move(command.split(" ")[1])
            elif command.startswith("take "):
                self.take_item(command.split(" ")[1])
            elif command == 'inventory':
                print("You have: " + ", ".join(self.inventory) if self.inventory else "Your inventory is empty.")
            else:
                print("I don't understand that command.")

    def move(self, direction):
        if direction == 'north' and self.current_room.north:
            self.current_room = self.current_room.north
            print(f"You moved north to the {self.current_room.name}.")
        elif direction == 'south' and self.current_room.south:
            self.current_room = self.current_room.south
            print(f"You moved south to the {self.current_room.name}.")
        elif direction == 'east' and self.current_room.east:
            self.current_room = self.current_room.east
            print(f"You moved east to the {self.current_room.name}.")
        elif direction == 'west' and self.current_room.west:
            self.current_room = self.current_room.west
            print(f"You moved west to the {self.current_room.name}.")
        else:
            print("You can't go that way.")

    def take_item(self, item):
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(f"You took the {item}.")
        else:
            print(f"There is no {item} here.")

# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()
