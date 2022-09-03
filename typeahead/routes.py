from typeahead import app

@app.route('/get-memo')
def get_memo():
    return {
        'success': True,
        'memory_usage': app.trie.get_size(),
    }


@app.route("/<query>")
def fast_search(query):
    return {
        "success": True,
        "found_items": app.trie.prefix_search(query),
    }
