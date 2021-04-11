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


def calculate_final_rate(faculty, speciality, rate1, rate2, rate3, rate4):
    try:
        rate1 = float(rate1)
        rate2 = float(rate2)
        rate3 = float(rate3)
        rate4 = float(rate4)
    except:
        return "Не правильні данні"
    rates = [rate1, rate2, rate3, rate4]
    result = 0
    subjects = coef[faculty][speciality]

    i = 0
    for position in subjects:
        result += float(list(subjects[position].values())[0]) * float(rates[i])
        i += 1
    result += 0.1 * float(rates[3])

    return result
