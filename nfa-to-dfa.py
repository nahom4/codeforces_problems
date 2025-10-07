from collections import deque

def epsilon_closure(nfa, states):
    """Compute the ε-closure of a set of NFA states."""
    closure = set(states)
    queue = deque(states)
    
    while queue:
        state = queue.popleft()
        # Check for ε-transitions from 'state'
        for (src, sym, dest) in nfa['transitions']:
            if src == state and sym == 'ε' and dest not in closure:
                closure.add(dest)
                queue.append(dest)
    return frozenset(closure)  # Use frozenset for hashability

def nfa_to_dfa(nfa):
    """Convert an NFA (with ε) to a DFA using subset construction."""
    alphabet = nfa['alphabet'] - {'ε'}  # Exclude ε from input symbols
    dfa = {
        'states': set(),
        'alphabet': alphabet,
        'transitions': {},
        'start_state': None,
        'accept_states': set()
    }
    
    # Step 1: Compute initial DFA state (ε-closure of NFA's start state)
    start_closure = epsilon_closure(nfa, {nfa['start_state']})
    dfa['start_state'] = start_closure
    dfa['states'].add(start_closure)
    
    # Step 2: Process unmarked states
    unmarked_states = [start_closure]
    
    while unmarked_states:
        current_state = unmarked_states.pop()
        
        # Step 3: For each input symbol, compute transitions
        for symbol in alphabet:
            # Find all NFA states reachable on 'symbol' from current_state
            next_states = set()
            for nfa_state in current_state:
                for (src, sym, dest) in nfa['transitions']:
                    if src == nfa_state and sym == symbol:
                        next_states.add(dest)
            
            # Compute ε-closure of these next states
            if next_states:
                new_dfa_state = epsilon_closure(nfa, next_states)
            else:
                new_dfa_state = frozenset()  # Dead state
            
            # Add transition
            dfa['transitions'].setdefault(current_state, {})[symbol] = new_dfa_state
            
            # If new_dfa_state is new, add it to unmarked_states
            if new_dfa_state not in dfa['states'] and new_dfa_state:
                dfa['states'].add(new_dfa_state)
                unmarked_states.append(new_dfa_state)
    
    # Step 4: Mark accept states (any DFA state containing an NFA accept state)
    for state in dfa['states']:
        if any(s in nfa['accept_states'] for s in state):
            dfa['accept_states'].add(state)
    
    return dfa

nfa = {
    'states': {'q0', 'q1', 'q2', 'q3', 'q4'},
    'alphabet': {'a', 'b', 'ε'},
    'transitions': [
        ('q0', 'ε', 'q1'),
        ('q0', 'ε', 'q2'),
        ('q1', 'a', 'q3'),
        ('q3', 'a', 'q3'),
        ('q2', 'b', 'q4'),
        ('q4', 'b', 'q4')
    ],
    'start_state': 'q0',
    'accept_states': {'q3', 'q4'}
}

dfa = nfa_to_dfa(nfa)
print("DFA States:", dfa['states'])
print("DFA Transitions:", dfa['transitions'])
print("DFA Accept States:", dfa['accept_states'])