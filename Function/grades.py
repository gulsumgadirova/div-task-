def get_grade(score):
    if score < 0 or score > 100:
        return "Yanlis bal"
    elif score >= 91:
        return "A"
    elif score >= 81:
        return "B"
    elif score >= 71:
        return "C"
    elif score >= 61:
        return "D"
    elif score >= 51:
        return "E"
    else:
        return "F"

    def make_report(students):
        report = {}
        for name in students:
            score = students[name]
            grade = get_grade(score)
            report[name] = grade
        return report

    students = {
        "Aysel": 95,
        "Murad": 72,
        "Elvin": 48
    }
    result = make_report(students)
    print(result)
       