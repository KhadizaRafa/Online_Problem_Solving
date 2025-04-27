# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s
# Mem
#


######## Solution  ########
# def max_split(str):
#     l=0
#     merged_string_list=[]
#     new_str_R=new_str_L=''
#     while (l <= len(str) + 1):
#         if (new_str_R and new_str_L) and len(new_str_L) == len(new_str_R):
#             merged_string_list.append(new_str_L + new_str_R)
#             new_str_L = ''
#             new_str_R = ''
#             continue
#         if l >= len(str):
#             break
#         if str[l] == 'R':
#             new_str_R=new_str_R + str[l]
#             l=l + 1
#         else:
#             new_str_L=new_str_L + str[l]
#             l=l + 1
#
#     return merged_string_list


def max_split(str):
    counter = 0
    for i in range(len(str)):
        counter = counter+2

input_str = input()
res_list = max_split(input_str)
# print(len(res_list))
# for i in res_list:
#     print(i)





# str = list('LLRRLLLRRR')
# print(str)
# l = 0
# merged_string_list = []
# new_str_R = new_str_L = ''
# while(l<=len(str)+1):
#     if (new_str_R and new_str_L) and len(new_str_L)==len(new_str_R):
#         merged_string_list.append(new_str_L+new_str_R)
#         new_str_L = ''
#         new_str_R = ''
#         continue
#     if l>=len(str):
#         break
#     if str[l] == 'R':
#         new_str_R = new_str_R+ str[l]
#         l = l+1
#     else:
#         new_str_L=new_str_L + str[l]
#         l=l + 1
