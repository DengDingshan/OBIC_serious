#somthing wrong, not finished
#trying to use ~ to convert the bin byte
def bitjudge(bitmasks,digit):
    #bitmasks is the string convert from data
    #digit can be a list or int
    if bitmasks != 0:
        output_bool = False
    else:
    #     magic_number = -4294967296
    # bitmasks_use = bitmasks - magic_number
        c = 0 # for judgment(combination)
        bitmasks_use = ~(bitmasks - 1)
        print(bitmaks_use) #bitmasks are dec
        if type(digit) == int:
            test_bin = '1' + digit*'0'
            test_dec = int(test_bin,2)
            c = test_dec & bitmasks_use;
        elif type(digit) == list:
            test_bin = 0
            for elements in digit:
                test_bin_line = int('1' + elements * '0') # change to int
                test_bin = test_bin + test_bin_line #test_bin is still an int now
            test_dec = int(str(test_bin),2) #str it then int test_bin to dec
            c = test_dec & bitmasks_use;
        else:
            print('something seems wrong(not int or list)')
        #test if c == the dec we need
        if c == test_dec:
            output_bool = True
        else:
            output_bool = False
    return output_bool

a = -2147481600
c = ~(a)
b = bitjudge(a,3)
print(bin(a),'\n',bin(c),b)
