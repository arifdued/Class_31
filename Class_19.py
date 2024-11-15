# # # # vowel = ['a','d','erg']

# # # # text_vwoles = 'damskfnaskfnasnk'

# # # # user_inp = input('enter a word')

# # # # if user_inp[-1] in vowel:
# # # #     print('ends whits vowels')
# # # # else:
# # # #     print('dosent ends whith Vowela')

# # # age = int(input('enter your age: '))
# # # if age<65:
# # #     print('old')
# # # elif age>= 18:
# # #     print('adult')
# # # else:
# # #     print('child')
    

    
# # # num = int(input('enter your num:'))
# # # if num == 0:
# # #     print('zero')
# # # elif num < 0 :
# # #     print('negetive number')
# # sentence=input("Enter your fav. sentence: ")

# # if sentence[-1] in "aeiouAIOU":

# #     print("The sentence ends with a vowel.")

# # else:

# #     print("The sentence ends with a consonant.")


# n = int(input('enter a number: '))
# n_2 = 0
# n_1 = 0
# for i  in range(n):
#     if i == 0 :
#         print(i,end=',')
#         n_1 = i
#     elif i == 0:
#         print(i)
#         n_2 = i
#         n_1 = n_2 + # temp
#         print(n_1,end=',')
         
# def Fact_n(num):
#     result = 1
#     if num == 0:
#         return 1
#     for i in range (1,num+1):
#         result = result * i
# #     return result
# # print(Fact_n(5))

lst = (1,2)

# lst.append(9)


try:
    lst.append(9)
    print(209/0)
except AttributeError:
    print('found an error that attributeerror ')