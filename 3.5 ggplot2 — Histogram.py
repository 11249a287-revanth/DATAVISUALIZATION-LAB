ggplot(students, aes(x = Math)) +
  geom_histogram(
    binwidth = 8,
    fill = "#9b59b6",
    color = "black",
    alpha = 0.8
  ) +
  geom_vline(
    aes(xintercept = mean(Math)),
    color = "red",
    linetype = "dashed",
    linewidth = 1
  ) +
  labs(
    title = "Distribution of Math Scores",
    x = "Score",
    y = "Count"
  ) +
  theme_classic()