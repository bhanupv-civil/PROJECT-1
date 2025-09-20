from os import scandir
def calculate_displacement(x, shape="square"):
    """
    Calculate the displacement for a given chamfer cut top width (x).
    
    :param x: The top width of the chamfer cut in mm.
    :param shape: The shape of the paver block ("square" or "hexagon").
    
    :return: Displacement in mm or a message indicating infeasibility.
    """
    
    # Check if the input width exceeds the maximum feasible value of 150 mm
    if x > 150:
        return "Not feasible: top width cut exceeds 150 mm."
    if x < 0:
        return "Not feasible: top width cut is below 0 mm."  
    
    # Calculate displacement based on shape
    if shape == "square":
        # Equation for square paver block
        U = (-7e-10) * x**4 + (2e-7) * x**2 + 0.0006*x + 2.275
    elif shape == "hexagon":
        # Equation for hexagonal paver block
        U = (-3e-10) * x**4 + (9e-8) * x**2 + 0.0007*x + 2.275
    else:
        raise ValueError("Shape must be either 'square' or 'hexagon'")
    
    return U


# Example usage
x_square = float(input("Enter the top width of chamfer cut for square block (in mm): "))
x_hexagon = float(input("Enter the top width of chamfer cut for hexagonal block (in mm): "))

# Calculate and print displacement for both blocks
displacement_square = calculate_displacement(x_square, shape="square")
displacement_hexagon = calculate_displacement(x_hexagon, shape="hexagon")
print()
print("Displacement for standard square paver block: 2.277*10^-3")
print(f"Displacement for SQUARE paver block with chamfer cut {x_square}:         {displacement_square} *10^-3mm")
print()
print("Displacement for standard hexagonal paver block: 2.277*10^-3")
print(f"Displacement for HEXAGONAL paver block with chamfer cut {x_hexagon}:       {displacement_hexagon} *10^-3mm")
