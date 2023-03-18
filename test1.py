n = int(input())
a = list(map(int, input().split()))

left, right = 0, 0
current_sum = a[0]
count = 0

while left < n and right < n:
    if current_sum == 0:
        count += 1
        right += 1
        if right < n:
            current_sum += a[right]
    elif current_sum < 0:
        right += 1
        if right < n:
            current_sum += a[right]
    else:
        left += 1
        if left < n:
            current_sum -= a[left-1]

print(count)
