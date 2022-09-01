def run():
    my_list = [e for e in range(1, 100) if e % 2 == 0]
    my_dict = {i: round(i**2, 2) for i in range(1, 101) if i % 2 == 0}
    print(my_dict)

if __name__ == '__main__':
    run()