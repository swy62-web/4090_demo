from pathlib import Path 
import sys
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from calculator_app import add

def test_add_1():
    assert add(5, 6) == 11

def test_add_2():
    assert add(6, 6) == 12
    