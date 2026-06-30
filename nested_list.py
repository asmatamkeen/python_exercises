students = []
scores = []
if __name__ == '__main__':

    for _ in range(int(input("enter n:"))):
        name = input("Enter name:")
        score = float(input("enter score:"))
        students.append([name,score])
        scores.append(score)
scores = list(set(scores))
scores.sort()
slg=scores[1]
low_final =[student[0] for student in students if student[1] == slg]
low_final.sort()
for name in low_final:
    print(name)
