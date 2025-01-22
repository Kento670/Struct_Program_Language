import re

# Define patterns for tokens
patterns = [
    [r"\d+", "number"],
    [r"\+", "+"],
    [r"\-", "-"],
    [r"\*", "*"],
    [r"\/", "/"],
    [r"\()", "()"],
    [r"\)", ")"],
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
        assert match
        # (process errors)
        token = {
            "tag":tag,
            "position":position,
            "value":match.group(0)
        }
        if token["tag"] == "number":
            token["value"] = int(token["value"])
        tokens.append(token)
        position = match.end()
    # append end-of-stream marker
    token.append({
        "tag":None,
        "value":None,
        "position":position
    })
    return tokens 

def test_simple_token():
    print("test simple token")
    examples = "+-*/"
    for example in examples:
        t = tokenize(example) [0]
        assert t["tag"] == example
        assert t["position"] == 0
        assert t["value"] == example


def test_number_token():
    print("test number tokens")
    for s in ["1","11"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "number"
        assert t[0]["value"] == int(s)

def test_mulitple_tokens():
    print("testing mulitple tokens")
    token = tokenize("1+2")
    print(tokens)
    exit(0)


if __name__ == "__name__":
    test_simple_token()
    test_number_token()
    test_mulitple_tokens()
