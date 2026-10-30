import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Hours_Studied"],
    df["Math"],
    c=df["Math"],
    cmap="viridis",
    s=100,
    edgecolors="black"
)

for i, name in enumerate(df["Student"]):
    plt.annotate(
        name,
        (df["Hours_Studied"][i], df["Math"][i]),
        textcoords="offset points",
        xytext=(5, 5),
        fontsize=8
    )

plt.colorbar(label="Math Score")
plt.title("Hours Studied vs Math Score")
plt.xlabel("Hours Studied per Day")
plt.ylabel("Math Score")
plt.tight_layout()

plt.savefig("scatter.png", dpi=150)
plt.show()
