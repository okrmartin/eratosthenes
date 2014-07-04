
def eratosthenes(limit):
    candidate_list = [x for x in range(2, limit)]
    prime_list = []
    
    while len(candidate_list) > 0:
        prime = candidate_list[0]
        prime_list.append(prime)
        sieve(prime, candidate_list)
        
    return prime_list

    
def sieve(number, candidate_list):
    multiple = multipleOf(number)
    multValue = multiple.next()
    
    last_value = candidate_list[-1]
    
    while multValue <= last_value:
        
        if multValue in candidate_list:
            candidate_list.remove(multValue)
        
        multValue = multiple.next()


def multipleOf(number):
    i = 1
    while True:
        yield i * number
        i = i + 1
        

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="n first prime numers")
    args = parser.parse_args()
    
    limit = args.n + 1
    prime_list = eratosthenes(limit)
    
    print prime_list