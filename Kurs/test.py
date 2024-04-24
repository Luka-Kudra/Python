def create_multidimensional_list(rows, columns):
    multidimensional_list = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = input(f"Enter element for row {i+1} and column {j+1}: ")
            row.append(element)
        multidimensional_list.append(row)
    return multidimensional_list

def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    multidimensional_list = create_multidimensional_list(rows, columns)

    print("\nYour multidimensional list:")
    for row in multidimensional_list:
        print(row)

if __name__ == "__main__":
    main()

