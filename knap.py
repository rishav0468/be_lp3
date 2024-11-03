def knap(cap, weight, value, n):

    # Create a 2D list `dp` with dimensions (n + 1) x (cap + 1)
    dp = [[0 for i in range(cap + 1)] for j in range(n + 1)]  # list comprehension

    # Start filling the dp table
    for i in range(1, n + 1):
        for j in range(1, cap + 1):  # Start from 1 because the first row and column are initialized to zero for base cases
            if weight[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], value[i - 1] + dp[i - 1][j - weight[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][cap]

# Input the capacity of the bag and number of items
cap = int(input("Capacity of bag: "))
n = int(input("Enter number of items: "))

# Input weights and values of items
weight = []
value = []
for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    v = int(input(f"Enter value of item {i + 1}: "))
    weight.append(w)
    value.append(v)

# Get the maximum value of the knapsack and print it
maxvalue = knap(cap, weight, value, n)
print("Max value of the bag is:", maxvalue)
