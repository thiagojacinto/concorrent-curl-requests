# concurrent-curl-requests
Python script to execute curl requests

## Usage

With [Python 3.10](https://www.python.org/downloads/) installed, clone this repository by doing:

```bash
# clone this repo
git clone https://github.com/thiagojacinto/concurrent-curl-requests.git

# then go the project directory
cd concurrent-curl-requests
```

### Command-line Interface (CLI) tool

The built-in CLI was developed to give more context of the parallel execution. To use just call the `cli.py` with the following commands:

```bash
python3 cli.py

# Or see more use cases by running the following:
python3 cli.py --help
```

### Python module

You may want to run this code as a simple python script, so just run the following commands: 

```bash
# Using the python script
python3 get_server_info_parallel.py
```

## Objective

Changing a little from the bash scripting habit. Simple usage of Python's own modules and concurrent benefits and availability of well known `curl` lib to handle HTTP requests. 

Made just for learning purposes. And fun. Have fun while using it!

## Colaborate

Feel free to give opinions, feedbacks or raise concerns at the [Issues](https://github.com/thiagojacinto/concurrent-curl-requests/issues) section. Any contribution is welcome! 🎉