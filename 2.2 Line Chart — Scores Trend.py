import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.plot(df["Student"], df["Math"],
         marker="o", label="Math", color="blue")

plt.plot(df["Student"], df["Science"],
         marker="s", label="Science", color="green")

plt.plot(df["Student"], df["English"],
         marker="^", label="English", color="red")

plt.title("Student Score Trends", fontsize=14)
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("line_chart.png", dpi=150)
plt.show()
