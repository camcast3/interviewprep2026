def unusual_traversal(array):
    if not array:
        return []
    n = len(array)
    mid = n // 2
    result = [array[mid]]
    
    step = 2
    left_covered = mid  # Track how far left we've already covered
    right_covered = mid + 1  # Track how far right we've covered

    while step <= n:
        # Left segment: from mid-step to left_covered
        left_start = mid - step
        if left_start < 0:
            left_start = 0
        if left_start < left_covered:
            result.extend(array[left_start:left_covered])
            left_covered = left_start  # Update coverage

        # Right segment: from right_covered to mid+1+step
        right_end = mid + 1 + step
        if right_end > n:
            right_end = n
        if right_covered < right_end:
            result.extend(array[right_covered:right_end])
            right_covered = right_end  # Update coverage

        step += 2
    
    return result