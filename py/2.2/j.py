n = int(input())
sum_1_2 = n // 100 + n // 10 % 10
sum_2_3 = n // 10 % 10 + n % 10
print(max(sum_1_2, sum_2_3), min(sum_1_2, sum_2_3), sep="")
