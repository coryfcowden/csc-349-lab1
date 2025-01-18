import sys #for taking in command line arguments

def find_singleton(nums):
    start = 0
    finish = len(nums) - 1

    #unless start == finish, divide and conquer
    while start < finish:
        #find mid
        mid = (start + finish) // 2

        #check if mid is a pair (not the single number)
        if mid % 2 == 0: #if mid has an even index
            if(nums[mid] == nums[mid+1]):
                #the single number must be to the right
                start = mid + 2
            else:
                #the single number must be to the left
                finish = mid
        else: #if mid has an odd index
            if(nums[mid] == nums[mid-1]):
                #the single number must be to the right
                start = mid + 1
            else:
                #the single number must be to the left
                finish = mid

    return nums[start]

def main():
    #take a command line argument from user
    arguments = sys.argv
    #make sure user followed correct template for input
    if len(arguments) != 2:
        print("Error! Command line argument must follow this form: python3 cfcowden_lab1.py unique-64")
        return
    
    #if correct number of arguments are supplied
        #store the second argument as the file name
    filename = arguments[1]

    #open file
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            numbers = [int(line.strip()) for line in lines]

        #if file opens, call find_singleton
        print(find_singleton(numbers))

    #if file does not open, throw exception
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()     