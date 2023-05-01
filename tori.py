# Test python env
def print_hello():
    anmils = ['dogs', 'cat', "hamster", "tiger"] # in one line
    foods = [
        'spahetti',
        'Pizza',
        'bibibob'
] # w/o triling comma
    names = [
        'John',
        'Jane',
        'Gil-dong',
        'Dong-eun'
] # w/ trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__=='__main__':
    print_hello()
