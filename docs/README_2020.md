> **Since 2020** — [Original README (2020)](docs/README_2020.md)

---

# Moth-Flame Optimization Algorithm (MFO) — Classic Documentation (2020)

> **Original documentation from the first release in 2020**
> Converted from `.rst` to `.md` for historical preservation.

---

## Introduction

Optimization refers to finding the best solution(s) for a problem. With increasing problem complexity, **metaheuristic algorithms** have become essential.

Traditional **mathematical optimization** is deterministic and often trapped in local optima.
**Metaheuristics** start from random solutions and improve iteratively.

Famous examples:
- Genetic Algorithm
- Grey Wolf Optimizer
- Ant Colony Optimization
- **Moth-Flame Optimization (MFO)**

---

## Moth-Flame Algorithm

Proposed by **Seyed Ali Mirjalili (2015)** in:
> *"Moth-flame optimization algorithm: A novel nature-inspired heuristic paradigm"*
> *Knowledge-Based Systems*, 2015.

### Inspiration: Transverse Orientation

Moths fly long distances at night using **transverse orientation** — maintaining a fixed angle with the **moon**.

![Moon Navigation](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.1.PNG?raw=true)

But around **artificial lights**, they spiral inward:

![Spiral Path](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.2.PNG?raw=true)

---

## MFO Model

- **Moths** = Candidate solutions  
- **Flames** = Best positions found so far  
- Moths update position around flames using **logarithmic spiral**

**Update Equation:**

$$M_i = D_i \cdot e^{b t} \cdot \cos(2\pi t) + F_j$$

**Distance to Flame:**

$$D_i = |F_j - M_i|$$

**Parameters:**
- $t \in [-1, 1]$: Controls closeness  
- $b$: Spiral shape
- **Flame count decreases linearly** → shifts from **exploration → exploitation**

---

## Population Matrices

```text
M = [m11, m12, ..., m1d]
    [m21, m22, ..., m2d]
    ...
    [mn1, mn2, ..., mnd]

OM = [f(m1), f(m2), ..., f(mn)]
```

---

## Spiral Update Visualization

![Spiral Update](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.8.PNG?raw=true)

---

## Conclusion

MFO models moth spiral behavior to converge solutions toward optimal flames.
Effective for **NP-Hard**, **continuous**, and **constrained** problems.

> **This document represents the original vision of the project in 2020.**

---

## ✉️ Contact

* Author: Hamed Babagheybi  
* Email: [hbabagheybi@gmail.com](mailto:hbabagheybi@gmail.com)  
* LinkedIn: [hamed-babagheybi](https://www.linkedin.com/in/hamed-babagheybi-06b1ba152)

---

[Back to Current README](../README.md)
