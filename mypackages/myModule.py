def top_n(items, n):
    """Return the top n items in an array , in desceding order.

      Args:
          items (array): list or array-like  object containging numerical values
          n (int): number of top items to be return.

      Returns:
              array: top n items , in descending order.

      Example:
          >>>top_n([8,7,3,9,11], 3)
          >>>[11,9,8]  
    """
    for i in range(n):  # keep sorting until we have top n numbers
        for j in range(len(items) - 1 - i):

            if items[j] > items[j + 1]:  # if this is bigger than the next item

                # swap the two numbers
                items[j], items[j + 1] = items[j + 1], items[j]
    top_n = items[-n:]  # Get last two items

    return top_n[::-1]


top_n([8, 3, 2, 7, 4], 3)
