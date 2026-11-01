ggplot(long_df, aes(x = Student, y = Score, fill = Subject)) +
  geom_bar(
    stat = "identity",
    position = "dodge"
  ) +
  scale_fill_brewer(palette = "Set1") +
  labs(
    title = "Scores by Student and Subject",
    x = "Student",
    y = "Score"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1)
  )