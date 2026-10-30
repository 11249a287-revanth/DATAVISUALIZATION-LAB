import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]

averages = [
    df["Math"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

plt.figure(figsize=(7, 5))

bars = plt.bar(
    subjects,
    averages,
    color=["#3498db", "#2ecc71", "#e74c3c"],
    edgecolor="black"
)

for bar, avg in zip(bars, averages):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() - 3,
        f"{avg:.1f}",
        ha="center",
        va="top",
        color="white",
        fontweight="bold"
    )

plt.title("Average Scores by Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("bar_chart.png", dpi=150)
plt.show()
