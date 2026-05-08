def print_array(arr):
    """
    Print each element of the list on a new line.
    """
    for item in arr:
        print(item)

def main():
    # Process integer list
    try:
        # Read the number of elements
        n_int = int(input().strip())
        int_list = []
        for _ in range(n_int):
            int_list.append(input().strip())
            
        # Process string list
        n_str = int(input("Enter the number of strings: ").strip())
        str_list = []
        for _ in range(n_str):
            str_list.append(input("Enter a string: ").strip())

        # Call the generic function
        print_array(int_list)
        print_array(str_list)
        
    except EOFError:
        pass

if __name__ == "__main__":
    main()