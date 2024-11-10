import pandas as pd

# Given array of items (Cost, Life, Value, Weight)
items = [(815, 3, 1, 13), (529, 3, 6, 18), (780, 5, 10, 2), (191, 11, 2, 11), (151, 7, 5, 43), (233, 1, 3, 24), 
         (217, 1, 5, 1), (980, 11, 2, 5), (789, 4, 7, 3), (609, 12, 6, 20), (864, 8, 10, 48), (154, 1, 2, 25), 
         (391, 2, 2, 4), (520, 4, 10, 36), (700, 1, 7, 3), (180, 4, 3, 11), (379, 8, 4, 21), (960, 9, 6, 31), 
         (344, 8, 2, 13), (655, 11, 8, 12), (381, 12, 2, 38), (640, 10, 3, 34), (366, 12, 10, 15), (310, 2, 7, 33), 
         (373, 8, 5, 45), (902, 9, 7, 9), (827, 1, 6, 46), (904, 2, 9, 26), (553, 4, 1, 3), (818, 10, 10, 40), 
         (820, 8, 5, 38), (889, 2, 3, 45), (403, 5, 4, 33), (876, 12, 4, 44), (818, 7, 3, 14), (848, 4, 10, 1), 
         (235, 5, 10, 14), (471, 3, 6, 4), (708, 8, 10, 3), (851, 4, 4, 43), (552, 10, 9, 39), (666, 9, 10, 47), 
         (727, 11, 4, 12), (248, 2, 1, 18), (521, 8, 2, 11), (224, 12, 4, 2), (750, 3, 1, 20), (970, 3, 5, 10), 
         (473, 2, 1, 33), (316, 7, 2, 4), (473, 11, 3, 20), (181, 6, 1, 44), (798, 1, 2, 33), (682, 9, 5, 7), 
         (389, 5, 3, 11), (448, 5, 9, 2), (298, 10, 8, 18), (240, 4, 6, 25), (495, 6, 1, 16), (928, 4, 5, 39), 
         (909, 12, 7, 18), (126, 9, 2, 27), (572, 2, 3, 1), (703, 8, 10, 12), (584, 5, 7, 28), (605, 8, 7, 25), 
         (919, 7, 8, 34), (928, 1, 3, 44), (342, 4, 1, 47), (969, 11, 4, 46), (444, 1, 5, 49), (804, 5, 1, 40), 
         (361, 4, 10, 7), (235, 7, 10, 40), (646, 8, 2, 36), (619, 4, 3, 16), (251, 1, 10, 46), (814, 6, 9, 49), 
         (204, 7, 8, 12), (126, 4, 5, 17), (377, 3, 4, 45), (952, 9, 2, 32), (639, 8, 3, 49), (878, 8, 7, 34), 
         (542, 6, 5, 25), (671, 8, 7, 19), (288, 8, 5, 44), (946, 6, 10, 33), (253, 8, 7, 15), (509, 5, 9, 21), 
         (596, 1, 10, 21), (303, 5, 8, 46), (330, 8, 9, 20), (730, 1, 4, 16), (117, 2, 2, 15), (727, 7, 1, 44), 
         (169, 7, 3, 25), (239, 1, 6, 36), (802, 10, 9, 45), (134, 3, 7, 17)]

# Create a DataFrame from the list of items
df = pd.DataFrame(items, columns=['Cost', 'Life', 'Value', 'Weight'])

# Calculate the priority for each item
df['Priority'] = (df['Cost'] + df['Value']) / df['Life']

# Sort items by priority in descending order
df = df.sort_values(by='Priority', ascending=False)

# Knapsack capacity (in tons)
capacity = 200

# Initialize total weight and value
total_weight = 0
total_value = 0
selected_items = []

# Iterate through sorted items
for i, row in df.iterrows():
    if total_weight + row['Weight'] <= capacity:
        # Add the whole item
        total_weight += row['Weight']
        total_value += row['Cost']
        selected_items.append((row['Cost'], row['Life'], row['Value'], row['Weight'], 'Full'))
    else:
        # Add a fraction of the item to fill the remaining capacity
        remaining_capacity = capacity - total_weight
        fraction = remaining_capacity / row['Weight']
        total_weight += remaining_capacity
        total_value += row['Cost'] * fraction
        selected_items.append((row['Cost'], row['Life'], row['Value'], remaining_capacity, f'Fraction {fraction:.2f}'))
        break

# Output the selected items, total weight, and total value
print(selected_items, total_weight, total_value)
