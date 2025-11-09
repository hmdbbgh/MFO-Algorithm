# Moth-Flame Optimization (MFO) Algorithm — Python Implementation

> **Nature-inspired metaheuristic optimization** based on the **spiral navigation of moths** around artificial lights.
> Introduced by **Seyedali Mirjalili (2015)** — *Knowledge-Based Systems*.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Last Updated](https://img.shields.io/badge/updated-2025-success.svg)](#)
[![GitHub stars](https://img.shields.io/github/stars/hmdbbgh/MFO-Algorithm?style=social)](https://github.com/hmdbbgh/MFO-Algorithm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/hmdbbgh/MFO-Algorithm?style=social)](https://github.com/hmdbbgh/MFO-Algorithm/network/members)

---

## Overview

**Moth-Flame Optimization (MFO)** is a **population-based metaheuristic** that simulates the **transverse orientation** of moths — flying at a fixed angle to light sources.

- **Natural**: Straight path to moon (distant light)
- **Artificial**: Spiral path around flame (near light) → **Inspires exploration & exploitation**

**Paper**: [Mirjalili, S. (2015)](https://doi.org/10.1016/j.knosys.2015.07.006)
**DOI**: `10.1016/j.knosys.2015.07.006`

---

## Concept: Nature → Algorithm

| Natural (Moon) | Artificial (Flame) |
|----------------|--------------------|
| ![Moon Navigation](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.1.PNG?raw=true) | ![Spiral Path](https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.2.PNG?raw=true) |

---

## Core Update Mechanism

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

## Quick Start

```bash
poetry install
poetry run mfo --fitness sphere --dim 10 --iters 100 --moths 50
```

> Report → `reports/sphere_report.txt`
> Plot → `reports/sphere_convergence.png`

---

## Example Convergence

```python
import matplotlib.pyplot as plt
plt.plot(best_fitness_curve)
plt.title("MFO on Sphere Function")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.grid(True)
plt.show()
```

---

## Project Structure

```bash
.
├── examples/          # CLI & benchmark scripts
├── src/mfo_algorithm/ # Core + fitness functions
├── tests/             # pytest unit tests
├── reports/           # Auto-saved results
├── docs/              # Historical docs
└── Media/Pics/        # Visual explanations
```

---

## Version History

| Version | Year | Notes |
|--------|------|-------|
| `v1.0` | **2020** | Initial release ([View Classic README](docs/README_2020.md)) |
| `v2.0` | **2025** | Modular, CLI, auto-reports, Persian support |

---

## Citation

```bibtex
@misc{babagheybi2025mfo,
  author = {Hamed Babagheybi},
  title = {Moth-Flame Optimization (MFO) — Python Implementation},
  year = {2025},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/hmdbbgh/MFO-Algorithm}}
}
```

---

## License

**MIT License** — Free for academic & commercial use.
See [`LICENSE`](LICENSE)

---

## خلاصه فارسی

الگوریتم **MFO** از رفتار **پرواز مارپیچی شب‌پره‌ها به دور شعله** الهام گرفته شده و برای حل مسائل **بهینه‌سازی پیوسته، گسسته و NP-Hard** بسیار مؤثر است.

**ویژگی‌های پیاده‌سازی**:
- اجرای **CLI**
- بنچمارک خودکار
- نمودار همگرایی
- ساختار ماژولار

---

## ✉️ Contact

* Author: Hamed Babagheybi  
* Email: [hbabagheybi@gmail.com](mailto:hbabagheybi@gmail.com)  
* LinkedIn: [hamed-babagheybi](https://www.linkedin.com/in/hamed-babagheybi-06b1ba152)

---

> **Project active since 2020** — See the [original 2020 documentation](docs/README_2020.md) for historical context.

