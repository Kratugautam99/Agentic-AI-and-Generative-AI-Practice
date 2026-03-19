# Tutorial: Creating a Calculator API with FastAPI and MCP
# This example shows how to combine FastAPI with MCP to create a web API

# Step 1: Import the required libraries
# FastAPI - for creating the web API
# FastApiMCP - for integrating FastAPI with MCP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

# Step 2: Create a FastAPI application
# This is the core of our web API
app = FastAPI(
    title="Calculator API Tutorial",
    description="A simple calculator API that demonstrates FastAPI and MCP integration",
    version="1.0.0"
)

# Step 3: Define API endpoints with FastAPI
# Each endpoint will be a POST request that accepts two numbers

@app.post("/add")
def add_numbers(a: float, b: float):
    """
    Add two numbers together.
    
    Parameters:
    - a (float): First number
    - b (float): Second number
    
    Returns:
    - dict: Contains the result of the addition
    """
    result = a + b
    return {"result": result, "operation": "addition"}

@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    """
    Subtract the second number from the first.
    
    Parameters:
    - a (float): Number to subtract from
    - b (float): Number to subtract
    
    Returns:
    - dict: Contains the result of the subtraction
    """
    result = a - b
    return {"result": result, "operation": "subtraction"}

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """
    Multiply two numbers together.
    
    Parameters:
    - a (float): First number
    - b (float): Second number
    
    Returns:
    - dict: Contains the result of the multiplication
    """
    result = a * b
    return {"result": result, "operation": "multiplication"}

@app.post("/divide")
def divide_numbers(a: float, b: float):
    """
    Divide the first number by the second.
    
    Parameters:
    - a (float): Number to divide (numerator)
    - b (float): Number to divide by (denominator)
    
    Returns:
    - dict: Contains either the result or an error message
    """
    # Error handling for division by zero
    if b == 0:
        return {
            "error": "Division by zero is not allowed",
            "operation": "division"
        }
    result = a / b
    return {"result": result, "operation": "division"}

# Step 4: Create an MCP wrapper for our FastAPI application
# This allows our API to be used as an MCP service
mcp = FastApiMCP(
    app,
    name="Calculator API with MCP",
    description="A calculator service that provides both HTTP API and MCP interfaces"
)

# Step 5: Mount the HTTP interface
# This makes our API accessible via HTTP
mcp.mount_http()

# Step 6: Start the server
if __name__ == "__main__":
    import uvicorn
    print("Starting the Calculator API server...")
    print("Once running, you can access:")
    print("- API documentation at: http://localhost:8002/docs")
    print("- Alternative API docs at: http://localhost:8002/redoc")
    uvicorn.run(app, host="localhost", port=8002)

# Try it out!
# 1. Run this script
# 2. Open your browser and go to http://localhost:8002/docs
# 3. You'll see the Swagger UI where you can test all endpoints
# 4. The service is also available as an MCP service!