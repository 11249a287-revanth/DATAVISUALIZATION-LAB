import matplotlib.pyplot as plt
import seaborn as sns

numeric_df = df[
    ["Math", "Science", "English", "Hours_Studied"]
]

corr = numeric_df.corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("heatmap.png", dpi=150)
plt.show()