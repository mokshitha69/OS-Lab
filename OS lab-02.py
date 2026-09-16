n = int(input("Enter number of processes: "))

at = []
bt = []

for i in range(n):
    at.append(int(input("Enter arrival time: ")))
    bt.append(int(input("Enter burst time: ")))

ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n
done = [False] * n

time = 0

for x in range(n):
    index = -1
    shortest = 9999

    for i in range(n):
        if not done[i] and at[i] <= time and bt[i] < shortest:
            shortest = bt[i]
            index = i

    if index == -1:
        time += 1
        continue

    time += bt[index]
    ct[index] = time
    tat[index] = ct[index] - at[index]
    wt[index] = tat[index] - bt[index]
    rt[index] = wt[index]
    done[index] = True

print("\nProcess\tAT\tBT\tCT\tTAT\tWT\tRT")

for i in range(n):
    print("P" + str(i + 1), "\t", at[i], "\t", bt[i],
          "\t", ct[i], "\t", tat[i], "\t", wt[i], "\t", rt[i])

print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)
print("Average Response Time =", sum(rt) / n)
print("Average Completion Time =", sum(ct) / n)