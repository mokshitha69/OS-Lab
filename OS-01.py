n = int(input("Enter number of processes: "))

bt = []
for i in range(n):
    bt.append(int(input("Enter burst time for P" + str(i + 1) + ": ")))

wt = [0] * n
tat = [0] * n

for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1]

for i in range(n):
    tat[i] = wt[i] + bt[i]

print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")

for i in range(n):
    print("P" + str(i + 1), "\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])

print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)