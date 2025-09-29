def input_is_valid(msg,start=0,end=None) -> int:
    """
    parameter : mgs,mulai dari satu sampai terakhit

    this fuction can be erro if,parameter is out or no 
    """
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print("Invalid input, Try again!")

        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print("Invalid range, Try again!")
            else:
                return int(inp)
            
        else:
            return int(inp)
