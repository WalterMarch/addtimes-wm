import sys


def add_time(this_total, this_in):
    # time string should be checked
    
    # split and set up time lists
    tot_nums = this_total.split(":")
    in_nums = this_in.split(":")

    if len(tot_nums) != len(in_nums):
        if len(tot_nums) < len(in_nums):
            tot_nums.insert(0, "00")
        else:
            in_nums.insert(0, "00")

    for i in range(0, (-1 * len(in_nums)), -1):
        slice_total = int(tot_nums[i - 1]) + int(in_nums[i - 1])
        
        if (slice_total > 60) and ((i - 1) != -3):
            slice_total = slice_total % 60
            tot_nums[i - 2] = int(tot_nums[i - 2]) + (slice_total // 60) + 1
        
        tot_nums[i - 1] = str(slice_total).zfill(2)
    
    new_total = ":".join(tot_nums)

    return new_total


my_in = "x"
total = "00:00:00"

while my_in != "0":
    my_str = "Enter HH:MM:SS or MM:SS; 0 to end: "

    if sys.version_info[0] >= 3:
        my_in = input(my_str)
    else:
        my_in = raw_input(my_str)

    if my_in != "0":
        total = add_time(total, my_in)
        print(total)
