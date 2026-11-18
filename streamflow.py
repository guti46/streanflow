# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

# river data
data = np.genfromtxt("June-2021-Provo-River-Streamflow-Rates.csv", delimiter=",", skip_header=1, dtype=str)

# dates
x = data[:, 0]

# river flow
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)


y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)
# check
print(x[:5])
print(y_1[:5])


# river graph
plt.figure(figsize=(10, 6))

plt.plot(x, y_1, label="Site 10163000")
plt.plot(x, y_2, label="Site 10155200")

plt.plot(x, y_3, label="Site 10155500")
plt.plot(x, y_4, label="Site 10154200")
plt.plot(x, y_5, label="Site 10155000")

# labels it
plt.title("Provo River Streamflow June 2021")
plt.xlabel("Date")

plt.ylabel("Streamflow (cfs)")

plt.xticks(range(0, len(x), 96), x[::96], rotation=45)

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

