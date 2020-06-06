import functools
def result_func(func):
    '''Function which prints result if data valid else print info about error'''
    @functools.wraps(func)
    def wrapp_func(*args,**kwargs):
        try:
            result = f'{func(*args,**kwargs)}'
        except BaseException as e:
            result = f'info about exception: \n {e}'
        print(result)
    return wrapp_func

def create_list(nums):
    '''Function which creating a list of numbers'''
    list_nums = []
    for i in range(0,len(nums)):
        list_nums.append(int(nums[i]))
    return list_nums

def sum_searh(sum, nums):
    '''Function which search pairs with required sum'''
    list_res=[]
    for i in nums:
        for j in nums:
            if j >= i and (j + i) == sum:
                list_res.append(f'{i} + {j}')
    list_set = list(set(list_res))
    return list_set

@result_func
def main():
    num = input("Enter the numbers: ").split()
    req_sum = int(input("Enter required sum:"))
    list_num = create_list(num)
    lis_res = sum_searh(req_sum,list_num)
    for i in range(0, len(lis_res)):
        print(lis_res[i])


if __name__ == '__main__':
    main()