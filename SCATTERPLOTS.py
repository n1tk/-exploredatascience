import numpy as np
from matplotlib import pyplot as plt
from numpy import loadtxt
from numpy import transpose

data0 = np.loadtxt("GPAData.txt")
data = transpose(data0)
gpa = data[1,]
exam = data[2,]
year = data[4,]

gpa2024 = gpa[0:200]
gpa2026 = gpa[400:600]

exam2024 = exam[0:200]
exam2026 = exam[400:600] ### exam grades class of 2026

plt.scatter(gpa2024,exam2024, s = 40, color = '#5D5166', marker = 'D', label = "Class of 2024")
plt.scatter(gpa2026,exam2026, s = 40, color = '#FF971C', marker = 'o', label = "Class of 2026")
plt.title("Class of 2024 vs. Class of 2026")
plt.legend(loc = 'lower left')
plt.xlabel("GPA")
plt.ylabel("Exam Score")
plt.axis([0, 4.1, 0, 101])
plt.show()
