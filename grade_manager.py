"""简单的学生成绩管理程序 / 간단한 학생 성적 관리 프로그램"""


def average(scores):
    """计算平均分 / 평균 점수 계산"""
    return sum(scores) / len(scores) if scores else 0


def grade(score):
    """把分数换算成等级 / 점수를 등급으로 변환"""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main():
    students = {
        "김민준": [92, 88, 95],
        "李华": [78, 85, 80],
        "Alex": [65, 59, 70],
        "Tom": [],
    }
    print(f"{'姓名/이름':<10}{'平均/평균':>10}{'等级/등급':>10}")
    for name, scores in students.items():
        if not scores:
            print(f"{name:<10}{'N/A':>10}{'N/A':>10}")
            continue
        avg = average(scores)
        print(f"{name:<10}{avg:>10.1f}{grade(avg):>10}")


if __name__ == "__main__":
    main()
