import pandas as pd
import numpy as np

class salaries:
    def __init__(self, file):
        self.file = file
        self.data = pd.read_csv(file)

    def read_employee_data(self):
        try:
            employee_data = self.data.copy()
            employee_data['Basic Salary'] = employee_data['Basic Salary'].astype(float)
            employee_data['House Rent Allowance'] = employee_data['House Rent Allowance'].astype(float)
            employee_data['Travel Allowance'] = employee_data['Travel Allowance'].astype(float)
            employee_data['Income Tax'] = employee_data['Income Tax'].astype(float)
            employee_data['Insurance'] = employee_data['Insurance'].astype(float)
            employee_data['ESIC'] = employee_data['ESIC'].astype(float)
            employee_data['Professional Tax'] = 200.0
        except:
            print("Data is incomplete")
        return employee_data

    def gross_net(self):
        employee_data = self.read_employee_data()

        # Convert relevant columns to NumPy arrays
        try:
            basic_salary = employee_data['Basic Salary'].values
            hra = employee_data['House Rent Allowance'].values
            ta = employee_data['Travel Allowance'].values
            esic = employee_data['ESIC'].values
            provident_fund = employee_data['Provident Fund'].values
            income_tax = employee_data['Income Tax'].values
            insurance = employee_data['Insurance'].values

            # Calculate gross salary
            gross_salary = np.sum([basic_salary, hra, ta, esic], axis=0)

            # Calculate net salary
            net_salary = gross_salary - provident_fund - insurance - 200 - (income_tax * gross_salary)
        except:
            print("Data is Incomplete")
        # Create a new DataFrame with gross and net salaries
        result_df = pd.DataFrame({'Employee ID': employee_data['Employee ID'], 'Gross Salary': gross_salary, 'Net Salary': net_salary})

        print("Gross salaries of all employees:")
        print(result_df[['Employee ID', 'Gross Salary']])
        print("\n\n")
        print("Net salaries of all employees:")
        print(result_df[['Employee ID', 'Net Salary']])


    def linear_min_max(self):
        employee_data = self.read_employee_data()

        # Find the minimum and maximum basic salaries using Pandas
        min_index = employee_data['Basic Salary'].idxmin()
        max_index = employee_data['Basic Salary'].idxmax()

        min_employee = employee_data.loc[min_index]
        max_employee = employee_data.loc[max_index]

        return min_employee, max_employee, max_employee['Basic Salary'], min_employee['Basic Salary']

    
    def divide_and_conquer_min_max(self, employee_data, low, high):
        if low == high:
            return employee_data['Basic Salary'][low], employee_data['Basic Salary'][low], low, low

        if high == low + 1:
            if employee_data['Basic Salary'][low] < employee_data['Basic Salary'][high]:
                return employee_data['Basic Salary'][low], employee_data['Basic Salary'][high], low, high
            else:
                return employee_data['Basic Salary'][high], employee_data['Basic Salary'][low], high, low

        mid = (low + high) // 2
        min1, max1, min_ind1, max_ind1 = self.divide_and_conquer_min_max(employee_data, low, mid)
        min2, max2, min_ind2, max_ind2 = self.divide_and_conquer_min_max(employee_data, mid + 1, high)

        if min1 < min2:
            overall_min = min1
            min_ind = min_ind1
        else:
            overall_min = min2
            min_ind = min_ind2

        if max1 > max2:
            overall_max = max1
            max_ind = max_ind1
        else:
            overall_max = max2
            max_ind = max_ind2

        return overall_min, overall_max, min_ind, max_ind    
salar = salaries(r"C:\Users\Vansh_Prac\SY_Prac\Python\DAA-LAB\employee_data.csv")

print(salar.divide_and_conquer_min_max(salar.data, 0, len(salar.data)-1))

print(salar.gross_net())