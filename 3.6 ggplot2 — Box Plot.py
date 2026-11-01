ggplot(long_df, aes(x = Subject, y = Score, fill = Subject)) +
  geom_boxplot(alpha = 0.7, outlier.colour = "red") +
  geom_jitter(width = 0.2, alpha = 0.5) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Score Distribution by Sub",
    x = "Subject", 
    y = "Score"
  ) +
  theme_light() +
  theme(legend.position = "none")