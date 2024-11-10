# life and value
# (cost + value) / life 
# less life, high cost be shipped earlier
# Consider a XYZ courier company. They receive different goods to transport to different cities. 
# Company needs to ship thegoods based on their life and value. Goods having less shelf life and high cost shall be shipped earlier. 
# Consider list of 100 such items and capacity of transport vehical is 200 tones. 
# Implement Algorithm for fractional knapsack problem.
import random
import pandas as pd

class knap:
    def __init__(self, c):
        self.items = []
        self.capacity = 200
        self.c = c
        self.df = pd.DataFrame(columns=['Cost', 'Life', 'Weight'])
    
    def items_input(self):
        # we need three fields per item
        # cost (100-1000 dollars), shelf life (1-12 months), value (1-10 scale) and weight (1-50 tonnes)
        for _ in range(100):
            cost = random.randint(100, 1000)
            life = random.randint(1, 12)
            weight = random.randint(1, 50)

            self.items.append((cost, life, weight))
        self.df = pd.DataFrame(self.items, columns=['Cost', 'Life', 'Weight'])
        self.df.to_csv(fr'C:\Users\Vansh_Prac\SY_Prac\Python\DAA-LAB\Lab5\items{self.c}.csv', index=False)
        return self.items
    
    def fractional(self):
        self.items = []
        if not self.items:
            return "Items is empty, please run the items_input function"
        else:
            self.df['Priority'] = self.df['Cost'] / self.df['Life']
            self.df = self.df.sort_values(by = 'Priority', ascending = False)

            total_weight = 0
            total_value = 0
            selected_items = []

            for i, row in self.df.iterrows():
                if total_weight + row['Weight'] <= self.capacity:
                    total_weight += row['Weight']
                    total_value += row['Cost']
                    selected_items.append((row['Cost'], row['Life'], row['Weight'], 'Full'))
                else:
                    remaining_capacity = self.capacity - total_weight
                    fraction = remaining_capacity / row['Weight']

                    fractional_value = row['Cost'] * (remaining_capacity / row['Weight'])
                    total_weight += remaining_capacity
                    total_value += fractional_value
                    selected_items.append((row['Cost'], row['Life'], remaining_capacity, f'Fraction {fraction:.2f}'))
                    break
        return selected_items, total_weight, total_value
        
    def display_selected_items(self, selected_items):
        df_selected = pd.DataFrame(selected_items, columns=['Cost', 'Life', 'Weight', 'Status'])

        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        pd.set_option('display.colheader_justify', 'center')

        print(df_selected.to_string(index=False))

    def main(self):
        print("\n\nMaking the Items by Price Range, Shelf Life and Value: ")
        if self.c != 2:
            print("Items array is: \n", self.items_input())
            print(f"Items have been saved to items{self.c}.csv")
        print("Selecting items based on their cost, and weight with fractional knapsack logic:\n")
        try:
            selected_items, total_weight, total_value = self.fractional()
            self.display_selected_items(selected_items)
            print(f"Total Weight: {total_weight}")
            print(f"Total Cost: {total_value}")
        except:
            print("Items array is empty: ", self.items)
        
        

knapsack = knap(2)
knapsack.main()

# for i in range(1, 6):
#     knapsack = knap(i)
#     knapsack.main()
        