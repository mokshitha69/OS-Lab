n = int(input("Enter number of processes: "))

at = []
bt = []

for i in range(n):
    at.append(int(input("Enter arrival time for P" + str(i + 1) + ": ")))
    bt.append(int(input("Enter burst time for P" + str(i + 1) + ": ")))

fta = [0] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n

time = 0

for i in range(n):

    if time < at[i]:
        time = at[i]

    fta[i] = time
    rt[i] = fta[i] - at[i]

    time = time + bt[i]
    ct[i] = time

    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nProcess\tAT\tBT\tFTA\tCT\tTAT\tWT\tRT")

for i in range(n):
    print("P" + str(i + 1), "\t",
          at[i], "\t",
          bt[i], "\t",
          fta[i], "\t",
          ct[i], "\t",
          tat[i], "\t",
          wt[i], "\t",
          rt[i])

print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)
print("Average Response Time =", sum(rt) / n)