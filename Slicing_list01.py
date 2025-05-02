def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.

    """
    b=[]
    for i in range(len(numbers)):
        if i%2==0:
            b.append(numbers[i])
    return b
print(main([9]))
