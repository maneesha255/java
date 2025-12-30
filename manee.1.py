def differenceofSum(n,m):
 sum_divisible=0
 sum_not_divisible=0
 for i in range(1,m+1):
     if i%n==0:
         sum_divisible+=i
        else:
            sum_not_divisible+=i
        return sum_not_divisible_sum_divisible

# Sample inputs
n=int(input("Enter n:"))
m=int(input("Enter m:"))
result =different of sum(n,m)
print("Difference=",result)
