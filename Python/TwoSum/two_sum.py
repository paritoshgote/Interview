def two_sum(nums, target):
    hash_map = {}
    for i, v in enumerate(nums):
        if target-v in hash_map:
            return [hash_map[target-v], i]
        else:
            hash_map[v] = i
    raise ValueError("No two sum match to target.")

def main():
    nums = [2,3,4,6,3,6,4]
    target = 8
    print(two_sum(nums, target))

if __name__=="__main__":
    main()