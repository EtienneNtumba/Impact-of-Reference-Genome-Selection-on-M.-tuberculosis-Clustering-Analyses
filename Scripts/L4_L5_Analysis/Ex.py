import sys
print("Python search paths:", sys.path)

try:
    from tools import ace_tools as tools
    print("Imported ace_tools successfully")
except ImportError as e:
    print(f"Error importing ace_tools: {e}")
    # Handle the error or exit
