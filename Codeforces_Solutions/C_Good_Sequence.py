





def good_seq(n,nums):
    i = 0
    while(i!=n):
        sub = nums.count(i) - int(i)
        if sub>0:
            i = i-1
        i = i+1
    return nums















# input_str = input()
res_list = good_seq(6,[1,2,2,3,3,3])
print(res_list)