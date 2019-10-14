import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # yapf: disable
    #parser.add_argument('-a', '--address', type=str,             help='Database address for the inserter',   default='127.0.0.1')
    parser.add_argument('-a', '--address', type=str,             help='Database address for the inserter',   default='192.168.10.11')
    parser.add_argument('-p', '--port', type=int,                help='Database port for the inserter',      default=2281)
    parser.add_argument('-i', '--inserter', action='store_true', help='To start inserter instead of the server')
    parser.add_argument('-c', '--color', action='store_true',    help='To force colored output')
    # yapf: enable

    args = parser.parse_args()
    if args.inserter:
        from financesSQL import inserter
        inserter.Inserter(ip=args.address, port=args.port, override_color=args.color)

    else:
        from financesSQL import main
        main()