#! python3
"""
    usage: roll [-h] [-v] [-n] expression [expression ...]
    
    Command Line Interface for the xdice library
    
    positional arguments:
      expression      mathematical expression(s) containing dice <n>d<s> patterns
    
    optional arguments:
      -h, --help      show this help message and exit
      -v, --version   print the xdice version string and exit
      -n, --num_only  print numeric result only (default is a verbose result)
"""
import argparse
import xdice

def main():
    parser = argparse.ArgumentParser(
        prog="roll", description="Command Line Interface for the xdice library"
    )
    parser.add_argument(
        "expression",
        nargs="+",
        help="mathematical expression(s) containing dice <n>d<s> patterns",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="print the xdice version string and exit",
    )
    parser.add_argument(
        "-n",
        "--num_only",
        action="store_true",
        help="print numeric result only (default is a verbose result)",
    )
    args = parser.parse_args()

    if args.version:
        print("XDice {}".format(xdice.__VERSION__))
        return
    
    for expr in args.expression:
        ps = xdice.roll(expr)
        
        if args.num_only:
            print(ps)
        else:
            print("{}\t({})".format(ps, ps.format(True)))


if __name__ == "__main__":
    main()
