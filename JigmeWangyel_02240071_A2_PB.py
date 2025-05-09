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

       
        index = NumberInPokedex - 1  
        page_number = index // self.page_size + 1
        position_on_page = index % self.page_size
        row = position_on_page // 8 + 1 
        col = position_on_page % 8 + 1   

        
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


binder = PokemonBinder()
binder.run()

#Technical Details:
    # Each binder page holds 64 cards in an 8x8 grid.
    # The Page number is calculated as:
    # page_number = (n - 1) // 64 + 1
    # The Explanation is:
    # Subtracting 1 makes indexing based by 0 
    # Dividing by 64 gives the 0 based page index number.
    # Adding of 1 converts it back to 1 based page from 0 based numbering for user friendly purpose.
#Document the Coordinate System Implementation:
    # The Rows and coloumn range from 1 till 8.
    # To calculate the position of a card with Pokedex number n:
    #     index_on_page = (n - 1) % 64
    #     row = index_on_page // 8 + 1  → Gets 1-based row number
    #     col = index_on_page % 8 + 1   → Gets 1-based column number
    # This allows the card to be placed from left to right and top to bottom order.
#Describe the Chosen In-Memory Data Structure and Its Operations
    # In-memory data structure:
    # A dictionary called cards is used to store Pokedex numbers as keyss.
    # The Values are tuples containing (page_number, (row, col)).
    # Some of the Operations are:
    # Adding, which inserts the key if it doesn't exist.
    # Lookup, which Checks if a card exists by using the in operator.
    # Reset, which Clears the entire dictionary using .clear().
    # Get score, which Uses len(cards) to count the number of unique cards.
#Explain Any Additional Data Structures Chosen and Why
    # The only data structure required for this program is a dictionary, which provides:
    # O(1) which is an average case time for insert, lookup, and delete
    # Easy mapping from Pokedex number to location

    # No additional structures were required as the dictionary handles both:
    # Card uniqueness is used as keys
    # Placement metadata as values
#Document the Reset Implementation 
    # The reset function is used to:
    # Ask the user for confirmation by typing in the word "CONFIRM"
    # If the user confirmes, it clears the cards dictionary using self.cards.clear()
    # It also resets the score to 0 from the score gained by the user
    # Display a confirmation message upon successful reset assuring the user about the deletion or reset
    # If not confirmed, no changes are made and a cancellation message is shown by typing of the word "EXIT"
#Explain the Data Deletion Process
    # Data deletion is done in-memory where no file or database is used.
    # When reset_binder() is called:
    # The dictionary storing all card placements is cleared thorugh .clear()
    # The score counter is reset to 0 from the users score before
    # This effectively erases all cards and placements from the current session and resets it to default
    # Since this is a runtime-only program, all data will also be erased from the program exit
