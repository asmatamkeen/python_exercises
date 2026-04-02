student_marks={
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}

student_grade={
    
}

for name, marks in student_marks.items():
    if marks >= 91:
        grade='A+'
        
    elif marks >=81:
        grade='A'
    
    elif marks >=71:
        grade='B+'

    elif marks >=61:
        grade='B'

    elif marks >=51:
        grade='C'

    elif marks >=41:
        grade='D'
    
    else:
        grade='F'

    
    student_grade[name]=grade
print(student_grade)

    