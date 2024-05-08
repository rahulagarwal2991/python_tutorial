# Handling CSV file
import csv
with open("emp.csv", "w", newline='') as f:
    w = csv.writer(f) # csv object
    w.writerow(["id", "name", "salary"])
    n = int(input("Enter no of employees"))
    for i in range(n):
        eno = input("Enter id : ")
        ename = input("Enter name : ")
        esalary = input("Enter salary : ")
        w.writerow([eno,ename, esalary ])

print("data inserted successfully")