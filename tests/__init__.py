import sys
from pathlib import Path

current_path = Path(__file__)
project_path = current_path.parent.parent.absolute()

sys.path.insert(0, str(project_path))
