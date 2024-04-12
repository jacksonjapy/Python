import random

def check_drunk_driving():
    alcohol_content = random.randint(0, 200)
    if alcohol_content < 20:
        return "不构成饮酒驾驶行为"
    elif 20 <= alcohol_content < 80:
        return "饮酒驾驶"
    else:
        return "醉酒驾驶"

print(check_drunk_driving())