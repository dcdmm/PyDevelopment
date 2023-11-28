from setuptools import setup, find_packages


extras_require = {}

package_name = "mypackage"

# 分析:
# 1. find_packages(where=".") ===>['atest', 'mypackage', 'mypackage1', 'mypackage.mp0', 'mypackage.my1']
# 2. find_packages(where=".", exclude=("a*", ) ===> ['mypackage', 'mypackage1', 'mypackage.mp0', 'mypackage.my1']
# 3. 列表表达式if判断 ===> ['mypackage', 'mypackage1', 'mypackage.mp0']
# 故:安装的包有mypackage包、mypackage目录下的mp0包、mypackage1包
packages = [
    package
    for package in find_packages(where=".", # '.'表示当前目录
                                 exclude=("a*", ))
    if package == package_name or package == package_name + '1' or package.startswith(package_name + ".mp") 
] 

setup(
    # A string specifying the name of the package.
    name=package_name,  
    # # A string specifying the version number of the package.
    version='0.0.1',
    # A string describing the package in a single line.
    description="setuptools test",
    # A string specifying the author of the package.
    author="dcdmm",
    # A string specifying the email address of the package author.
    author_email="dcdmm@gmail.com",
    # A string specifying the URL for the package homepage.
    url="https://github.com/dcdmm/setuptools",
    # A list of strings or a comma-separated string providing descriptive meta-data.
    keywords=["python", "setuptools"],
    # A string specifying the license of the package.
    license="Apache 2.0 License",

    # A list of strings specifying the packages that setuptools will manipulate.
    packages=packages,
    # If set to True, this tells setuptools to automatically include any data files it finds inside your package directories that are specified by your MANIFEST.in file. For more information, see the section on Including Data Files(https://setuptools.pypa.io/en/latest/userguide/quickstart.html#including-data-files).
    include_package_data=True,

    # A string corresponding to a version specifier (as defined in PEP 440) for the Python version, used to specify the Requires-Python defined in PEP 345.
    python_requires=">=3.6.0",
    # A string or list of strings specifying what other distributions need to be installed when this one is. See the section on Declaring required dependency(https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#declaring-dependencies) for details and examples of the format of this argument.
    install_requires=[
        'tqdm',
        "numpy >= 1.9.0",
        "scipy >= 1.0.0",
        "scikit-learn >= 0.18.0",
        "colorama >= 0.4.6"
    ]
)