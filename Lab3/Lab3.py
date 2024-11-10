import csv

def read_employee_data(file):
    employee_data = []
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for i in reader:
            #(["Employee ID", "Basic Salary", "House Rent Allowance", "Travel Allowance", "Provident Fund", "Income Tax", "Insurance", "Professional Tax", "ESIC"])
            emp_id = i['Employee ID']
            basic_salary = float(i['Basic Salary'])
            hra = float(i['House Rent Allowance'])
            ta = float(i['Travel Allowance'])
            itax = float(i['Income Tax'])
            insurance = float(i['Insurance'])
            ptax = 200.0
            esic = float(i['ESIC'])
            employee_data.append((emp_id, basic_salary, hra, ta, itax, insurance, ptax, esic))
    return employee_data

def gross_net(employee_data): 
    #gross = basicsalary + HRA + TA + esic 
    #net = gross - totaltax - insurace 
    gross = [[i[0], int(i[1]+i[2]+i[3]+i[7])] for i in employee_data]
    net = [[i[0], int(i[1]+i[2]+i[3]+i[7] - (i[6]+i[4]*(i[1]+i[2]+i[3]+i[7]) + i[5]))] for i in employee_data]
    print("Gross salaries of all employees is: ", gross)
    print("Net salaries of all employees is: ", net)

def linear_min_max(employee_data):
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

    print(f"Employee with the Maximum Salary is: {employee_data[max_ind][0]} with a salary of {overall_max}")
    print(f"Employee with the Minimum Salary is: {employee_data[min_ind][0]} with a salary of {overall_min}")

def divide_and_conquer_min_max(employee_data, low, high):
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
    min1, max1, min_ind1, max_ind1 = divide_and_conquer_min_max(employee_data, low, mid)
    min2, max2, min_ind2, max_ind2 = divide_and_conquer_min_max(employee_data, mid + 1, high)
    
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

# Read the employee data
employee_data = read_employee_data(r"C:\Users\basud\Desktop\Prac\Python\2nd YEAR\Sem-3\DAA-LAB\employee_data.csv")

# overall_min, overall_max, min_ind, max_ind = divide_and_conquer_min_max(employee_data, 0, len(employee_data) - 1)

# print(f"Employee with the Maximum Salary is: {employee_data[max_ind][0]} with a salary of {overall_max}")
# print(f"Employee with the Minimum Salary is: {employee_data[min_ind][0]} with a salary of {overall_min}")


print("Finding the minimuim and maximum using Divide and Conquer:\n", divide_and_conquer_min_max(read_employee_data(r"C:\Users\basud\Desktop\Prac\Python\2nd YEAR\Sem-3\DAA-LAB\employee_data.csv"), 0, len(read_employee_data(r"C:\Users\basud\Desktop\Prac\Python\2nd YEAR\Sem-3\DAA-LAB\employee_data.csv"))-1))
print("Finding the minimum and maximum using Linear Checks:")
print(linear_min_max(read_employee_data(r"C:\Users\basud\Desktop\Prac\Python\2nd YEAR\Sem-3\DAA-LAB\employee_data.csv")))

print("Finding the minimuim and maximum using Divide and Conquer:\n", divide_and_conquer_min_max([], 0, 0))
print("Finding the minimum and maximum using Linear Checks:\n", linear_min_max([]))


gross_net(employee_data=read_employee_data(r"C:\Users\basud\Desktop\Prac\Python\2nd YEAR\Sem-3\DAA-LAB\employee_data.csv"))