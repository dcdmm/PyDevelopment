# As such, a valid Dockerfile must start with a FROM instruction.
# The image can be any valid image – it is especially easy to start by pulling an image from the Public
# The FROM instruction initializes a new build stage and sets the Base Image for subsequent instructions.
FROM python:3.8.15-slim-bullseye

# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.
#  If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction.
WORKDIR /my_code

# `COPY [--chown=<user>:<group>] <src>... <dest>`
# `COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]`
# The COPY instruction copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
# Multiple <src> resources may be specified but the paths of files and directories will be interpreted as relative to the source of the context of the build.
# Example:
# To add all files starting with “hom”: COPY hom* /my_code
# ? is replaced with any single character, e.g., “home.txt”.:COPY hom?.txt /mydir/
# The <dest> is an absolute path, or a path relative to WORKDIR, into which the source will be copied inside the destination container.
# The example below uses a relative path, and adds “test.txt” to <WORKDIR>/relativeDir/:COPY test.txt relativeDir/
# Whereas this example uses an absolute path, and adds “test.txt” to /absoluteDir/:COPY test.txt /absoluteDir/
# Note:
# The <src> path must be inside the context of the build; you cannot COPY ../something /something, because the first step of a docker build is to send the context directory (and subdirectories) to the docker daemon.
# If <src> is a directory, the entire contents of the directory are copied, including filesystem metadata.(The directory itself is not copied, just its contents)
# If <src> is any other kind of file, it is copied individually along with its metadata. In this case, if <dest> ends with a trailing slash /, it will be considered a directory and the contents of <src> will be written at <dest>/base(<src>).
# If multiple <src> resources are specified, either directly or due to the use of a wildcard, then <dest> must be a directory, and it must end with a slash /.
# If <dest> does not end with a trailing slash, it will be considered a regular file and the contents of <src> will be written at <dest>.
# If <dest> doesn’t exist, it is created along with all missing directories in its path.
COPY . /my_code
# 与上等价
# COPY . .

# The RUN instruction will execute any commands in a new layer on top of the current image and commit the results.
# The resulting committed image will be used for the next step in the Dockerfile.
RUN pip install -r requirements.txt

# There can only be one CMD instruction in a Dockerfile.
# If you list more than one CMD then only the last CMD will take effect.
# The main purpose of a CMD is to provide defaults for an executing container.
# Note:
# Do not confuse RUN with CMD. RUN actually runs a command and commits the result;
# CMD does not execute anything at build time, but specifies the intended command for the image.
# Note:
# If you want to run your <command> without a shell then you must express the command as a JSON array and give the full path to the executable.
# This array form is the preferred format of CMD.
# Any additional parameters must be individually expressed as strings in the array:
# CMD ["/usr/bin/wc","--help"]
CMD ["python", "app.py"]