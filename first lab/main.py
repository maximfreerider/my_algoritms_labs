from algoritms.student import Student
from algoritms.sorting import bubble_sort,quicksort
import time

if __name__ == "__main__":
    students = []
    lines = [line.rstrip('\n') for line in open('students_info_list.txt')]
    for line in lines:
        fields = line.split(',')
        student = Student(fields[0], fields[1], fields[2], fields[3])
        students.append(student)

    print("Bubble sort")
    start_time = time.perf_counter()
    bubble_sort(students)
    print("Time: " + str(time.perf_counter() - start_time))
    for item in students:
        print(item)

    print("Quick Sort")
    start_time = time.perf_counter()
    quicksort(students, 0, len(students)-1, 0)
    print("Time: " + str(time.perf_counter() - start_time))
    for item in students:
        print(item)


    # opened_list.append(Student('Max', 'Ivanov', 75, 45))
    # opened_list.append(Student('Vova', 'Vasylevich', 5, 55))
    # opened_list.append(Student('Ivan', 'Vovan', 25, 15))
    # opened_list.append(Student('Yura', 'Logan', 85, 95))