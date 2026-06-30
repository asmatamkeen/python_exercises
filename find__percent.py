if __name__ == '__main__':
    n = int(input("enter n:"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("enter name and scores:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter query name:")
score1 = student_marks[query_name]
avg=(sum(score1))/len(score1)
print(f"{avg:.2f}")