from .models import Student

def match_students(target_student_id):
    target_student = Student.objects.get(id=target_student_id)
    target_interests = set(target_student.interests.values_list('id', flat=True))

    matches = []
    for student in Student.objects.exclude(id=target_student_id):
        other_interests = set(student.interests.values_list('id', flat=True))
        if target_interests or other_interests:
            match_score = len(target_interests & other_interests) / len(target_interests | other_interests) * 100
        else:
            match_score = 0

        # Only add students with match_score > 0
        if match_score > 0:
            matches.append((student, round(match_score, 2)))

    # Sort matches in descending order of match_score
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches