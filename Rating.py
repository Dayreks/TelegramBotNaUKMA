from source import coef, faculty_json


def get_speciality(faculty):
    specialities = coef[faculty]
    specialities_string = []
    for speciality in specialities:
        specialities_string.append(speciality)
    return specialities_string


def get_subject(faculty, speciality):
    subjects = coef[faculty][speciality]
    subjects_arr = []
    for key in subjects:
        for subject in subjects[key]:
            subjects_arr.append(subject)
    return subjects_arr


def calculate_final_rate(faculty, speciality, rate):
    rate = rate.split(' ')
    if len(rate) < 4:
        return "Не правильні данні"
    result = 0
    subjects = coef[faculty][speciality]

    i = 0
    for position in subjects:
        result += float(list(subjects[position].values())[0]) * float(rate[i])
        i += 1
    result += 0.1 * float(rate[3])
    return result
