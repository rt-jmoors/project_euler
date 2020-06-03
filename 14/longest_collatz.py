# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it
# has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
import datetime

begin_time = datetime.datetime.now()

start_n = 1000000
chain_length = 0
max_chain = (start_n, chain_length)


def collatz(number):
    """Returns the next Collatz number in the sequence"""

    if number == 1:
        return 1

    if number % 2 == 0:
        # number must be even
        return number // 2
    else:
        return 3 * number + 1


limit = 1000000
# all_chains = {num : num_terms_in_collatz_chain}
all_chains = {1: 1, 2: 2}
i = 1

while i < limit:
    if i in all_chains.keys():
        print('already exists:\t', i, 'chain count: ', all_chains[i])
        i += 1
        continue

    seq_num = i
    current_collatz_chain = {i: 1}

    while seq_num != 1:
        if collatz(seq_num) in all_chains.keys():
            current_collatz_chain[seq_num] = 0
            for key in current_collatz_chain.keys():
                all_chains[key] = current_collatz_chain[key] + all_chains[collatz(seq_num)] + 1
            break
        else:
            current_collatz_chain[seq_num] = 0
            for key in current_collatz_chain.keys():
                current_collatz_chain[key] += 1
            seq_num = collatz(seq_num)

    current_collatz_chain = {}
    print('new number:\t', i, 'chain count: ', all_chains[i])
    i += 1

max_key = max(all_chains, key=all_chains.get)
print(max_key, all_chains[max_key])
