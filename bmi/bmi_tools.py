def calc_bmi(height, weight):
    if validate_height(height) & validate_weight(weight):
        return round((weight / (height * height)), 2)
    else:
        raise Exception("check height (m) and weight")


def validate_height(height):
    return height <= 2.5


def validate_weight(weight):
    return weight <= 160
