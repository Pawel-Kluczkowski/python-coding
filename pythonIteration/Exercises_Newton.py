def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better,"\n")
        if abs(approx - better) < 0.001:
            return better
        approx = better

# Test cases


print(sqrt(25.0))
