# Create student dataset
students <- data.frame(
  Student = c(
    "Srinivas", "Siva", "Naveen", "Srinath", "Ganesh",
    "Anil", "Deep", "Radhakrishna", "Kiran", "Harsha"
  ),
  Math = c(82, 72, 91, 65, 78, 85, 60, 95, 70, 83),
  Science = c(90, 82, 76, 88, 72, 80, 91, 85, 94, 80),
  English = c(91, 78, 89, 88, 86, 87, 83, 92, 97, 90),
  Hours = c(3, 4, 5, 7, 8, 10, 2, 4, 5, 6)
)

head(students)