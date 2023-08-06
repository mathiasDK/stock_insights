from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils.yf_extractor import YahooExtractor

if __name__ == "__main__":
    a = YahooExtractor("AAPL")