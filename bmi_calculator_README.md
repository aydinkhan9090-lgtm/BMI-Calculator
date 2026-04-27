<div align="center">

# 💪 BMI Calculator

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #5 — Enter your weight & height. Know your health instantly. 🖤**

</div>

---

## 💡 What It Does

```
Enter your weight in KG
Enter your height in CM
→ BMI calculated instantly
→ Tells you your health category!
```

---

## 🎮 Demo

```bash
WELCOME TO THE BMI CALCULATOR 💪
Enter your weight: 70
Enter your height in cm: 175
Your BMI is: 22.86
Your category is: Normal 🟩 (Healthy)
```

---

## ▶️ Run It

```bash
python BMI_calculator.py
```

---

## 🏥 BMI Categories

| BMI Range | Category | Status |
|-----------|----------|--------|
| Less than 18.5 | Underweight 😗 | Eat more! |
| 18.5 – 24.9 | Normal 🟩 | Perfect! |
| 25.0 – 29.9 | Overweight 🟨 | Exercise more! |
| 30 and above | Obese 🟥 | See a doctor! |

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `def calculate_bmi()` | Machine to calculate BMI |
| `def get_category()` | Machine to get health category |
| `float(input())` | Get decimal numbers from user |
| `return` | Send result out of function |
| `round(bmi, 2)` | Clean up long decimal numbers |
| `if / elif / else` | Check which category BMI falls in |

---

## 💻 Source Code

```python
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight 😗⬜"
    elif bmi < 24.9:
        return "Normal 🟩 (Healthy)"
    elif bmi < 29.9:
        return "Overweight 🟨"
    else:
        return "Obese 🟥"

print("WELCOME TO THE BMI CALCULATOR 💪")
weight = float(input("What is your weight: 😙 "))
height_cm = float(input("What is your height in cm: 🗼 "))
height_m = height_cm / 100

bmi = calculate_bmi(weight, height_m)
category = get_category(bmi)

print("Your BMI is:", round(bmi, 2))
print("Your category is:", category)
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
