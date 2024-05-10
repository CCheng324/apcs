# Read the input
taiwan_time = int(input())

# Calculate the US Mountain Time
us_mountain_time = (taiwan_time - 15) % 24

# Print the result
print(us_mountain_time)