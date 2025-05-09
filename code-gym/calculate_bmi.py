def bmi(weight, height):
    """
    Write function bmi that calculates body mass index (bmi = weight / height2).

    if bmi <= 18.5 return "Underweight"

    if bmi <= 25.0 return "Normal"

    if bmi <= 30.0 return "Overweight"

    if bmi > 30 return "Obese"
    """
    bmi = weight / height**2
#     if(bmi <= 18.5): return "Underweight"
#     if(bmi <= 25.0): return "Normal"
#     if(bmi <= 30.0): return "Overweight"
#     else: return "Obese"

    # categories = {
    #     (0, 18.5): "Underweight",
    #     (18.5, 25.0): "Normal",
    #     (25.0, 30.0): "Overweight",
    #     (30.0, float('inf')): "Obese"
    # }
    # for (low, high), category in categories.items():
    #     if low < bmi <= high:
    #         return category

    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi > 30) + (bmi > 25) + (bmi > 18.5)]

bmi(180, 75)
