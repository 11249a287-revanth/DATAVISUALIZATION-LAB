library(tidyr)
library(ggplot2)

Student <- data.frame(
  Student = c("S1", "S2", "S3", "S4"),
  Math = c(85, 90, 78, 88),
  Science = c(80, 85, 82, 90),
  English = c(75, 88, 80, 85)
)

long_df <- pivot_longer(
  Student,
  cols = c(Math, Science, English),
  names_to = "Subject",
  values_to = "Score"
)

ggplot(long_df,
       aes(x = Student, y = Score,
           color = Subject, group = Subject)) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  theme_minimal() +
  labs(title = "Student Score Trends",
       x = "Student", y = "Marks") +
  theme(axis.text.x = element_text(
    angle = 45, hjust = 1))