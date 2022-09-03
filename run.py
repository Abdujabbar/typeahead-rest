import time
from os.path import exists
from typeahead import app
from typeahead.data import get_contents
from typeahead.cli import parse
from typeahead.trie import build_trie

if __name__ == '__main__':
    args = parse()

    if not exists(args.data_path):
        raise Exception("File not found")
    print("Please be patient, while I load data store. . .")
    start = time.time_ns()
    app.trie = build_trie(get_contents(args.data_path))
    print(f"Elapsed time for build trie: {(time.time_ns() - start) / (10 ** 9)}s")
    print("Finished loading process. . . ")
    app.run(port=args.port, debug=True)