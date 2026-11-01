ggplot(students, aes(x = Hours, y = Math, label = Student)) +
  geom_point(aes(color = Math), size = 4) +
  geom_smooth(
    method = "lm",
    se = TRUE,
    color = "steelblue",
    linetype = "dashed"
  ) +
  geom_text(vjust = -1, size = 3) +
  scale_color_gradient(
    low = "orange",
    high = "darkblue"
  ) +
  labs(
    title = "Hours Studied vs Math Score",
    x = "Hours Studied",
    y = "Math Score"
  ) +
  theme_minimal()