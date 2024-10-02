num_of_clients = int(input().strip())
order_ids = list(map(int, input().strip().split()))

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

for order_id in order_ids:
    print(sum_of_digits(order_id), end=" ")