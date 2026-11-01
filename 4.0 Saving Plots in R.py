# Save last ggplot as PNG
ggsave(
  "scatter_r.png",
  width = 8,
  height = 5,
  dpi = 150
)

# Save base R plot as PNG
png("barplot_r.png", width = 800, height = 500)

# Create the base R bar chart
avgs <- colMeans(students[, c("Math", "Science", "English")])

barplot(
  avgs,
  main = "Average Subject Scores",
  xlab = "Subject",
  ylab = "Average Score",
  col = c("#3498db", "#2ecc71", "#e74c3c"),
  ylim = c(0, 100)
)

dev.off()