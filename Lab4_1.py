import random
import csv

class inversions:
    
    def __init__(self, c):
        self.courses = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
        self.students = []
        self.c = c

        # self.student_list_maker()
        self.create_csv()

        brute_inv_dict = self.total_inversions_brute()
        print(brute_inv_dict)
        merge_inv_dict = self.total_inversions_DAC()
        print(merge_inv_dict)

    def course_selector(self):
        return random.sample(self.courses, 5)
    
    def student_list_maker(self):
        students = self.students
        for _ in range(100):
            students.append(self.course_selector())
        return students

    def create_csv(self):
        filename = fr"C:\Users\Vansh_Prac\SY_Prac\Python\DAA-LAB\Lab4\students{self.c}.csv"
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Student', 'Courses'])
            for i, j in enumerate(self.students):
                writer.writerow([f'Student{i+1}'] + j)
        print(f"\nCSV file {filename[2:]} has been created!\n")

    def total_inversions_brute(self):
        total_inv = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        
        for courses in self.students:
            inv_count = self.inversion_counter_brute(courses)
            if inv_count in total_inv:
                total_inv[inv_count] += 1

        return total_inv

    def inversion_counter_brute(self, courses):
        inv = 0
        for i in range(len(courses)):
            for j in range(i+1, len(courses)):
                if courses[i] > courses[j]:
                    inv += 1
        return inv

    def total_inversions_DAC(self):
        inv_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for course in self.students:
            inv = self.count_invs_DAC(course[:])
            if inv in inv_counts:
                inv_counts[inv] += 1
        return inv_counts

    def count_invs_DAC(self, courses):
        
        if len(courses) < 2:
            return 0
        mid = len(courses) // 2
        left = courses[:mid]
        right = courses[mid:]

        inversions = self.count_invs_DAC(left) + self.count_invs_DAC(right)
        inversions += self.merge_and_count(courses, left, right)
        return inversions

    def merge_and_count(self, courses, left, right):
        i = j = k = 0
        inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                courses[k] = left[i]
                i += 1
            else:
                courses[k] = right[j]
                inversions += len(left) - i
                j += 1
            k += 1

        while i < len(left):
            courses[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            courses[k] = right[j]
            j += 1
            k += 1

        return inversions

def main():
    course_manager = inversions(3)
    course_manager.student_list_maker()
    brute = course_manager.total_inversions_brute()
    merge = course_manager.total_inversions_DAC()
    print("By the Brute Force Approach: ")
    for i, j in brute.items():
        print(f"The students with {i} inversion counts: {j}")
    print("\n")
    print("By the Merge Approach: ")
    for i, j in merge.items():
        print(f"The students with {i} inversion counts: {j}")
    
    
if __name__ == "__main__":
    main()