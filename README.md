# 🦋 Moth-Flame Optimization Algorithm (MFO)

> A modern, nature-inspired metaheuristic optimization algorithm based on the navigation behavior of moths around a flame.

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](#)
[![GitHub Stars](https://img.shields.io/github/stars/USERNAME/REPO.svg)](https://github.com/USERNAME/REPO/stargazers)
[![Last Updated](https://img.shields.io/badge/last%20update-2025-success.svg)](#)

---

## 📘 Overview

**Moth-Flame Optimization (MFO)** is a nature-inspired **metaheuristic algorithm** introduced by **Seyed Ali Mirjalili (2015)** in the paper:  
> *"Moth-Flame Optimization Algorithm: A Novel Nature-Inspired Heuristic Paradigm"*  
> *Knowledge-Based Systems, Volume 89, 2015.*

The MFO algorithm simulates the *transverse orientation* navigation of moths around light sources — a behavior that leads to efficient global exploration and local exploitation in the search space.

---

## 🌍 Concept & Intuition

Moths use a mechanism called **transverse orientation** to maintain a fixed angle with the moon for navigation.  
However, when exposed to artificial lights (close sources), this mechanism leads to a **spiral trajectory**, where moths eventually converge toward the flame.

This behavior is mathematically modeled to guide search agents (moths) toward optimal solutions (flames).

### Conceptual Illustration
| Natural vs Artificial Navigation |
|----------------------------------|
| ![Transverse Orientation](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.1.PNG) |
| ![Spiral Path Behavior](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.2.PNG) |

---

## ⚙️ Algorithm Description

Each moth represents a **candidate solution** in an *n × d* search space:  
- *n*: number of moths (population size)  
- *d*: number of dimensions (variables)

At each iteration, moths update their positions around flames using a **logarithmic spiral** defined as:

![Spiral Equation](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.6.PNG)

where:
- *D(i,j)* = distance between the i-th moth and the j-th flame  
- *b* = constant defining spiral shape  
- *t* = random number in [-1, 1]

This mechanism allows both **exploration** (searching wide areas) and **exploitation** (fine-tuning around best solutions).

![Moth Position Update](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.8.PNG)

---

## 🧮 Mathematical Model

Let:
- `M` = matrix of moths' positions (`n × d`)
- `F` = matrix of flames (`n × d`)
- `OM` = fitness array of moths  
- `OF` = fitness array of flames  

During each iteration:
```
for each moth i:
    update D(i) = |F_j - M_i|
    M_i = D(i) * exp(b * t) * cos(2πt) + F_j
```

Flames are updated based on the best fitness values found so far.  
The number of flames gradually decreases over iterations to balance exploration and exploitation.

---

## 🧠 Pseudocode

```
Initialize population M (moths)
Calculate fitness for all moths → OM
While termination condition not met:
    Sort moths based on fitness
    Update number of flames
    Update moth positions using logarithmic spiral
    Evaluate fitness and update OM
Return best flame as optimal solution
```

---

## 📊 Implementation Notes

- Any **random distribution** can be used for initialization (`uniform`, `normal`, etc.)
- The **spiral movement** ensures diverse exploration in early iterations and convergence in later stages.
- The algorithm can handle **continuous** and **NP-hard** optimization problems.

---

## 🚀 Applications

- Function optimization (benchmark functions)
- Feature selection
- Neural network training
- Engineering design optimization
- Energy management & load balancing

---

## 🧩 Example Output

Example of convergence curve (using Python implementation):

```python
import matplotlib.pyplot as plt
plt.plot(best_fitness)
plt.xlabel("Iteration")
plt.ylabel("Best fitness")
plt.title("MFO Convergence Curve")
plt.grid(True)
plt.show()
```

Resulting visualization:

![Convergence Plot](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.7.PNG)

---

## 📄 Reference

> Mirjalili, S. (2015). Moth-Flame Optimization Algorithm: A Novel Nature-Inspired Heuristic Paradigm.  
> *Knowledge-Based Systems*, 89, 228–249.  
> DOI: [10.1016/j.knosys.2015.07.006](https://doi.org/10.1016/j.knosys.2015.07.006)

---

## 🧭 Citation

If you use this repository, please cite as:
```
Author Name (2025). Moth-Flame Optimization (MFO) Algorithm — Implementation and Notes.  
GitHub Repository: https://github.com/USERNAME/REPO
```

---

## 🪪 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🇮🇷 About (Persian Summary)

الگوریتم **Moth-Flame Optimization (MFO)** یک روش بهینه‌سازی الهام‌گرفته از طبیعت است که بر اساس رفتار شب‌پره‌ها در پرواز به دور منبع نور مدل‌سازی شده.  
این روش در سال ۲۰۱۵ توسط **سیدعلی میرجلّیلی** ارائه شد و از آن زمان در بسیاری از مسائل بهینه‌سازی، از جمله شبکه‌های عصبی، انتخاب ویژگی و مسائل NP-Hard استفاده شده است.  

در این پیاده‌سازی:
- ساختار الگوریتم به شکل ماژولار بازنویسی شده است.  
- نمودارهای همگرایی و خروجی‌های قابل مشاهده اضافه شده‌اند.  
- کدها برای پژوهش و آموزش در دسترس هستند.  

📘 ریپو اصلی: [GitHub Repository](https://github.com/USERNAME/REPO)

---

## ✉️ Contact

- Author: Your Name  
- Email: your.email@example.com  
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
