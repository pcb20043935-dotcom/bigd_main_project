import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "AppleGothic" #윈도우는 Malgun Gothic

prices = [25780, 25975, 26025, 25865, 25980]
days = ["10. 02.", "10. 06.", "10. 07.", "10. 08.", "10. 12."]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, prices)

for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")

ax.set_title("TIGER 미국S&P500")
fig.savefig("my_first_chart.png")