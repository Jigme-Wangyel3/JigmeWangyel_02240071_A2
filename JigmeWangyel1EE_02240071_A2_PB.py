class PokemonBinder:
    def __init__(self, Maximum_Pokedex=1025, SizeOfPage=64):
        self.max_pokedex = Maximum_Pokedex
        self.page_size = SizeOfPage
        self.cards = {}

    def add_card(self, NumberInPokedex):
        if not (1 <= NumberInPokedex <= self.max_pokedex):
            return f"Invalid Pokedex number. Enter a number between 1 and {self.max_pokedex}."

        if NumberInPokedex in self.cards:
            page, pos = self.cards[NumberInPokedex]
            return f"Page: {page}, Position: {pos}, Status: Already exists"

        # Calculate page number and grid position
        index = NumberInPokedex - 1  # zero-based
        page_number = index // self.page_size + 1
        position_on_page = index % self.page_size
        row = position_on_page // 8 + 1  # 8x8 grid, 1-based row
        col = position_on_page % 8 + 1   # 1-based col

        # Store the card
        self.cards[NumberInPokedex] = (page_number, f"({row},{col})")
        return f"Page: {page_number}, Position: ({row},{col}), Status: Newly added"

    def reset_binder(self):
        self.cards.clear()
        return "Binder has been reset."

    def show_binder_status(self):
        sorted_cards = sorted(self.cards.items())
        for num, (page, pos) in sorted_cards:
            print(f"Pokedex #{num}: Page {page}, Position {pos}")
        total = len(self.cards)
        percent = (total / self.max_pokedex) * 100
        print(f"Total cards: {total}")
        print(f"Completion: {percent:.2f}%")
        if total == self.max_pokedex:
            print("You have caught them all!")

    def run(self):
        while True:
            print("\n--- Deep Pocket Monster: Pokemon Binder ---")
            print("1. Add a Pokemon card")
            print("2. Reset binder")
            print("3. Show binder status")
            print("4. Exit")
            choice = input("Select mode (1-4): ")

            if choice == "1":
                try:
                    number = int(input("Enter Pokedex number: "))
                    print(self.add_card(number))
                except ValueError:
                    print("Invalid input. Please enter a number.")

            elif choice == "2":
                print("WARNING: This will erase your entire binder.")
                confirm = input("Type CONFIRM to proceed or EXIT to cancel: ").strip().upper()
                if confirm == "CONFIRM":
                    print(self.reset_binder())
                elif confirm == "EXIT":
                    print("Reset cancelled.")
                else:
                    print("Invalid input. Reset not performed.")

            elif choice == "3":
                self.show_binder_status()

            elif choice == "4":
                print("Session ended. See you next time!")
                print(f"Total cards collected: {len(self.cards)}")
                break
            else:
                print("Invalid option. Please select 1-4.")


# Instantiate and run the binder
binder = PokemonBinder()
binder.run()
