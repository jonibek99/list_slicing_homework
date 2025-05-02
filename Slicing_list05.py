def main(list1,n,k):
    """
    A list of several elements is given. Return the value from n index to k index.
    Args:
        list1(list): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        list: return answer.
    """
    return list1[list1[n-1]:list1[k-1]:1]
print(main([1,2,3,4,5,6,7,8,9,10],3,7))