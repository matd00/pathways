import argparse

def main():
    parser = argparse.ArgumentParser(description="Pathways - Filaris - Fast Multithreaded Web Explorer")
    parser.add_argument("--url", required=True, help="Initial URL to start scanning")
    parser.add_argument("--match-str", default="", help="Only include URLs containing this string.")
    parser.add_argument("--max_urls", type = int, default = 1000, help = "Max numbers of URLs to discover.")
    parser.add_argument("--ignore", type = list, nargs= "*", default=[], help = "Ignore URLs containig this args(strings) " )
    parser.add_argument("--depth", type = int, default = 3, help="Numbers of Depths" )
    parser.add_argument("--concurrency", type=int, default=10, help="Number of concurrent tasks.")
    
    return parser.parse_args()

