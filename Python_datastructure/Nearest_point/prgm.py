def getcoordinates():
    input_str = input("Enter the list of coordinates (e.g., [(1,-2), (-2, 4), (-1,-1)]): ")
    coordinates = eval(input_str)
    return coordinates

def main():
    coordinates = getcoordinates()
    x_coords = [x for x, y in coordinates]
    y_coords = [y for x, y in coordinates]

    min_x = min(x_coords)
    min_y = min(y_coords)

    shift_x = abs(min_x) if min_x < 0 else 0
    shift_y = abs(min_y) if min_y < 0 else 0

    shifted_coordinates = [(x+shift_x, y+shift_y)for x,y in coordinates]
    
    print(shifted_coordinates)

if __name__ == "__main__":
    main()            
    


