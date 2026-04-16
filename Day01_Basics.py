import statistics

def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
    
    return {
        "Mean": mean,
        "Median": median,
        "Mode": mode
    }

# Example
nums = [1, 2, 2, 3, 4, 5]
result = calculate_stats(nums)
print(result)
