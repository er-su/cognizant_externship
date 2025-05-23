import pickle as pkl
from pathlib import Path
from typing import Dict, List, Tuple

class FinanceTracker():
    def __init__(self):
        self.pickle_path = Path("tracker.pkl")
        # Attempt to load in the serialized file
        self.tracker_dict: Dict[str, List[Tuple[str, float]]] = self.load_pickle()

    def save_pickle(self):
        with open(self.pickle_path, "wb") as f:
            pkl.dump(self.tracker_dict, f)

    def load_pickle(self):
        try:
            with open(self.pickle_path, "rb") as f:
                return pkl.load(f)
            
        except FileNotFoundError:
            return {}
        
    def run(self):
        while True:
            val = self.menu()
            match val:
                case 1:
                    self.add_expense()
                case 2:
                    self.view_summary()
                case 3:
                    self.view_expenses()
                case 4:
                    self.save_pickle()
                    print("See you next time!")
                    break

    def menu(self) -> int:
        print("what would you like to do?\n" \
        "1. Add Expense\n" \
        "2. View All Expenses\n" \
        "3. View Summary\n" \
        "4. Exit")

        while(True):
            try: 
                val = int(input("Choose an option: "))
            except ValueError:
                print("Please enter a number!")
                continue
            if val < 1 or val > 4:
                print("Not a valid selection! Please enter a different number")
                continue
            else:
                return val
    
    def add_expense(self):
        cat = input("Enter category: ").strip().lower().capitalize()
        desc = input("Enter expense description: ")

        while True:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Not a valid amount! Please try again")
            else:
                break
        self.tracker_dict.setdefault(cat, []).append((desc, amount))
        print("Expense added successfully")

    def view_expenses(self):
        if len(self.tracker_dict) == 0:
            print("You don't have any expenses! Go add some")
            return
        
        for cat, lis in self.tracker_dict.items():
            print(f"-----{cat}-----")
            for desc, amount in lis:
                print(f" - {desc} : {amount}")

    def view_summary(self):
        if len(self.tracker_dict) == 0:
            print("You don't have any expenses! Go add some")
            return
        
        print("-----Summary-----")
        for cat, lis in self.tracker_dict.items():
            total = sum(x[1] for x in lis)
            print(f" - {cat}: {total}")
    
ft = FinanceTracker()
ft.run()