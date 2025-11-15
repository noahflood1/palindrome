import argparse

parser = argparse.ArgumentParser(description="Demo of argparse")

# add arguments
parser.add_argument("filename", help="Name of the file to process")
parser.add_argument("--verbose", action="store_true", help="Enable logs") # optional flag
parser.add_argument("--count", type=int, default=1, help="How many times")

args = parser.parse_args()

print("File:", args.filename)
print("Verbose mode:", args.verbose)
print("Count:", args.count)


