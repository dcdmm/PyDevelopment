# The socket to bind.
# -b
bind = "0.0.0.0:5000"

# The number of worker processes for handling requests.
# Default: 1
workers = 4 
# -w

# The number of worker threads for handling requests.
# Run each worker with the specified number of threads.
# Default: 1
threads = 2 
# --threads

# workers = 4: 4个(worker)进程并发处理HTTP请求
# threads = 2: 每个(worker)进程同时并发处理2(每个worker进程内的线程数)个HTTP请求

# SSL key file
# Default: None
# keyfile = ""
# --keyfile

# SSL certificate file
# Default: None
# certfile = ""
# --certfile

# Workers silent for more than this many seconds are killed and restarted.
# Default: 30
timeout = 30
# -t

# The granularity of Error log outputs.
# Valid level names are:
# 'debug'
# 'info'
# 'warning'
# 'error'
# 'critical'
# Default: 'info'
loglevel = 'info'
# --log-level

# The Error log file to write to.
# Using '-' for FILE makes gunicorn log to stderr.
# Default: '-'
errorlog = "log/errorlog.log"
# --error-logfile

# The Access log file to write to.
# '-' means log to stdout.
# Default: None
accesslog = "-"
# --access-logfile

# Set environment variables in the execution environment.
# Default: []
# Should be a list of strings in the key=value format.
# For example on the command line: gunicorn -b 127.0.0.1:8000 --env FOO=1 test:app
# Or in the configuration file: raw_env = ["FOO=1"]
raw_env = []