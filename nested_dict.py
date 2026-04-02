
student_data=[
    {
        "Name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"Python"
    },
    {
        "Name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java"

    }
]


def add_new_student(name,roll_no,age,course):
    
    student_data.append({"Name":name,"roll_no":roll_no, "age":age, "course":course})

add_new_student("Shyam",22,16,"C++")
add_new_student("asma",22,16,"C++")

print(student_data)