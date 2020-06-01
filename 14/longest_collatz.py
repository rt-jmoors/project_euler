
max_chain = (0, 0)
chain_length = 0
start_n = 1000000

while start_n > 0:
    n = start_n
    while n != 1:
        chain_length += 1
        if n % 2 == 0:
            # even number
            n = n // 2
        else:
            # odd number
            n = 3 * n + 1
    chain_length = chain_length + 1

    print('starting number: ', start_n, 'chain length: ', chain_length)
    if max_chain[1] < chain_length:
        max_chain = start_n, chain_length

    chain_length = 0
    start_n -= 1

print('max chain = ', max_chain)