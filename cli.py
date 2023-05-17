import argparse

from get_server_info_parallel import (
        DOGS_LIST,
        execute_requests,
        run
    )

__version__ = "0.1.0"

def extendend_help_info() -> str:
    return """
    ######## Usage Examples ###########

        - python3 cli.py
            This will gather information about all dog breed's list.

        - python3 cli.py --breed beagle
            This will bring information about the informed dog breed

        - python3 cli.py -b beagle boxer
            This will bring information about the list of dog breeds.
    
        - python3 cli.py --breed not_registered
            If the breed informed is not found, the user will be notified by an error
    
        - python3 cli.py --list [-l]
            Displays a list of valid dog breeds to choose from.

    ###################################
    """

def display_available_breeds():
    return print(DOGS_LIST)

parser = argparse.ArgumentParser(
    description="CLI for sending parallel HTTP requests",
    epilog=extendend_help_info(),
    formatter_class=argparse.RawDescriptionHelpFormatter,
    allow_abbrev=False
)

parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s {}".format(__version__))

parser.add_argument(
    "--breed", "-b",
    type=str,
    nargs="+",
    help="The dog's breed that an image will be retrieved",
    choices=DOGS_LIST
)

parser.add_argument(
    "--list", "-l",
    help="Display a list of available dog breeds and exit",
    action="store_true",
    default=False
)

args = parser.parse_args()

breed = args.breed

if args.list:
    display_available_breeds()
elif breed:
    print("[DEBUG] Breed(s): {}".format(breed))
    run(execute_requests(breed))
else:
    run(execute_requests(DOGS_LIST))