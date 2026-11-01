import matplotlib.pyplot as plt
import seaborn as sns

melted = df.melt(
    id_vars="Student",
    value_vars=["Math", "Science", "English"],
    var_name="Subject",
    value_name="Score"
)

plt.figure(figsize=(8, 5))

sns.boxplot(
    x="Subject",
    y="Score",
    data=melted,
    palette=["#3498db", "#2ecc71", "#e74c3c"]
)

plt.title("Score Distribution by Subject (Box Plot)")
plt.tight_layout()

plt.savefig("boxplot.png", dpi=150)
plt.show()