import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # yapf: disable
    #parser.add_argument('-a', '--address', type=str,             help='Database address for the inserter',   default='127.0.0.1')
    parser.add_argument('-a', '--address', type=str,                  help='Database address for the inserter',   default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int,                     help='Database port for the inserter',      default=1234)
    parser.add_argument('-g', '--generate_base', action='store_true', help='To generate base db info')
    # yapf: enable

    args = parser.parse_args()
    if args.generate_base:
        from .models import generate_base
        generate_base()

    else:
        from . import main
        main(host=args.address, port=args.port)