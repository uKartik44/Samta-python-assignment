def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    # Input values for length and width from the user
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    # Call the calculate_area function
    result = calculate_area(length, width)

    # Display either the area or the message
    print("Area:", result)

if __name__ == "__main__":
    main()
