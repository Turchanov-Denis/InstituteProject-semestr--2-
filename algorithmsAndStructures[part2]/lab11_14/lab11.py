def compute_transition_function(pattern):
    m = len(pattern)
    alphabet = set(pattern)
    transition_function = [{char: 0 for char in alphabet} for _ in range(m + 1)]
    for state in range(m + 1):
        for char in alphabet:
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[:next_state] != pattern[state - next_state + 1:state] + char:
                next_state -= 1
            transition_function[state][char] = next_state
    return transition_function

def search(pattern, text):
    n = len(text)
    m = len(pattern)
    transition_function = compute_transition_function(pattern)
    state = 0
    for i in range(n):
        state = transition_function[state].get(text[i], 0)
        if state == m:
            print("Pattern found at index", i - m + 1)

pattern = "abc"
text = "ababcababcabc"
search(pattern, text)
