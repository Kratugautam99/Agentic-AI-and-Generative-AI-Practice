# Tutorial: Creating a Simple Calculator MCP Service
# This is a step-by-step guide to creating a calculator service using FastMCP

# Step 1: Import the FastMCP library
# FastMCP is a framework that helps us create Model Context Protocol (MCP) services
from fastmcp import FastMCP

# Step 2: Create an MCP service instance
# Give your service a meaningful name that describes what it does
mcp = FastMCP(name="Tutorial Calculator")

# Step 3: Define your first tool - Addition
# The @mcp.tool() decorator tells FastMCP that this function should be exposed as a tool
@mcp.tool(
    # You can customize the tool's properties
    name="add",  # The name that will be used to call this tool
    description="Add two numbers together",  # A clear description of what the tool does
    tags={"math", "arithmetic"}  # Optional tags to categorize your tool
)
def add_numbers(x: float, y: float) -> float:
    """Add two numbers together.
    
    Args:
        x (float): The first number to add
        y (float): The second number to add
    
    Returns:
        float: The sum of the two numbers
    """
    return x + y

# Step 4: Define more tools - Subtraction
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.
    
    Args:
        a (float): The number to subtract from
        b (float): The number to subtract
    
    Returns:
        float: The difference between the numbers
    """
    return a - b

# Step 5: Add multiplication
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together.
    
    Args:
        a (float): The first number to multiply
        b (float): The second number to multiply
    
    Returns:
        float: The product of the two numbers
    """
    return a * b

# Step 6: Add division with error handling
@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second.
    
    Args:
        a (float): The number to divide (numerator)
        b (float): The number to divide by (denominator)
    
    Returns:
        float: The quotient of the division
        
    Raises:
        ValueError: If attempting to divide by zero
    """
    # Important: Always check for division by zero!
    if b == 0:
        raise ValueError("Cannot divide by zero! Please use a non-zero divisor.")
    return a / b

# Step 7: Run the service
# This is where we start our MCP service
if __name__ == "__main__":
    # The run() method starts the service using STDIO (standard input/output) by default
    print("Starting the Calculator MCP service...")
    mcp.run()  # This will keep running until you stop the program

# Try it out!
# Once you run this script, you can use these calculator functions through any MCP client
# Each function (add, subtract, multiply, divide) will be available as a tool