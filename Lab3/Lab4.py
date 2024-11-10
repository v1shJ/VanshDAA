import csv
import pandas as pd

class salaries:
    def __init__(self, file):
        self.file = file
        data = pd.read_csv(file)

    def read_employee_data(self, file):
        employee_data = []
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                #(["Employee ID", "Basic Salary", "House Rent Allowance", "Travel Allowance", "Provident Fund", "Income Tax", "Insurance", "Professional Tax", "ESIC"])
                try:
                    emp_id = i['Employee ID']
                    basic_salary = float(i['Basic Salary'])
                    hra = float(i['House Rent Allowance'])
                    ta = float(i['Travel Allowance'])
                    itax = float(i['Income Tax'])
                    insurance = float(i['Insurance'])
                    ptax = 200.0
                    esic = float(i['ESIC'])
                    employee_data.append((emp_id, basic_salary, hra, ta, itax, insurance, ptax, esic))
                except:
                    print("Data is not complete")
                    break
        return employee_data


    def gross_net(self): 
        #gross = basicsalary + HRA + TA + esic 
        #net = gross - totaltax - insurace 
        employee_data = self.read_employee_data(self.file)
        gross = [[i[0], int(i[1]+i[2]+i[3]+i[7])] for i in employee_data]
        net = [[i[0], int(i[1]+i[2]+i[3]+i[7] - (i[6]+i[4]*(i[1]+i[2]+i[3]+i[7]) + i[5]))] for i in employee_data]
        print("Gross salaries of all employees is: ", gross)
        print("\n\n")
        print("Net salaries of all employees is: ", net)


    def linear_min_max(self):
        employee_data = self.read_employee_data(self.file)
        if employee_data == []:
            return -1
        overall_min, overall_max = float('INF'), float('-INF')
        for i in range(len(employee_data)):
            if float(employee_data[i][1]) > overall_max:
                overall_max = float(employee_data[i][1])
                max_ind = i
            elif float(employee_data[i][1]) < overall_min:
                overall_min = float(employee_data[i][1])
                min_ind = i

        return employee_data[max_ind], employee_data[min_ind], overall_max, overall_min


    def divide_and_conquer_min_max(self, employee_data, low, high):
        if low == high and low == 0:
            return -1
        if low == high:
            return employee_data[low][1], employee_data[low][1], low, low
        
        if high == low + 1:
            if employee_data[low][1] < employee_data[high][1]:
                return employee_data[low][1], employee_data[high][1], low, high
            else:
                return employee_data[high][1], employee_data[low][1], high, low
        
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

        return overall_min, overall_max, min_ind+1, max_ind+1
    

salar = salaries(r"C:\Users\Vansh_Prac\SY_Prac\Python\DAA-LAB\employee_data.csv")
salar.gross_net()