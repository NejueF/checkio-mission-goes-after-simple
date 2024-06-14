"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['world', 'w', 'o'],
            "answer": True,
        },
        {
            "input": ['world', 'w', 'r'],
            "answer": False,
        },
        {
            "input": ['world', 'l', 'o'],
            "answer": False,
        },
        {
            "input": ['list', 'l', 'o'],
            "answer": False,
        },
        {
            "input": ['', 'l', 'o'],
            "answer": False,
        },
        {
            "input": ['list', 'l', 'l'],
            "answer": False,
        },
        {
            "input": ['world', 'd', 'w'],
            "answer": False,
        },
        #I suggest these changes because without them the problem can be solved with the wrong code
        {
            "input": ['mankind', 'n', 'n'],
            "answer": False,
        },
    ],
    "Extra": [
        {
            "input": ['cable', 'l', 'b'],
            "answer": False,
        },
        {
            "input": ['cable', 'a', 'b'],
            "answer": True,
        },
        {
            "input": ['copyrightable', 'o', 'p'],
            "answer": True,
        },
        {
            "input": ['copyrightable', 'o', 'a'],
            "answer": False,
        },
        {
            "input": ['copyrightable', 'o', 'o'],
            "answer": False,
        },
    ]
}
