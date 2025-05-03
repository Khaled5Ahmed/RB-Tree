from rbTree import RBTree 

class Menu:
    def __init__(self):
        self.tree = RBTree()
        self.tree.load_dictionary()

    def show(self):
        while True:
            print("\nDictionary Menu:")
            print("1. Insert a new word")
            print("2. Search for a word")
            print("3. Show tree size")
            print("4. Show tree height")
            print("5. Show black height")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                word = input("Enter the word to insert: ").strip()
                self.tree.insert(word)

            elif choice == "2":
                word = input("Enter the word to search: ").strip()
                self.tree.check_word(word)

            elif choice == "3":
                print("Tree size:", self.tree.get_size())

            elif choice == "4":
                print("Tree height:", self.tree.get_tree_height())

            elif choice == "5":
                print("Black height:", self.tree.get_black_height())

            elif choice == "6":
                print("Exiting.")
                break
            else:
                print("Invalid choice! Try again.")