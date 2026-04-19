import sys
from pathlib import Path

#---------------------------------------------------------------
lib_path = Path(__file__).parent.parent
lib_path = lib_path.resolve()
sys.path.insert(0, str(lib_path))
#---------------------------------------------------------------