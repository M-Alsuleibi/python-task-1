import sys
from cli import run

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "inventory.csv"
    run(filepath)