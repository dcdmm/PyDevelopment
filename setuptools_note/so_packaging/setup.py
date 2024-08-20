from setuptools import setup, find_packages

# setuptools打包pybind11 + cmake生成的动态库文件(WSL2 Ubunut20.04base环境中测试)

setup(
    name="xyzasdf",
    version="0.0.1",
    packages=find_packages(),
    # A dictionary mapping package names to lists of glob patterns.
    # For a complete description and examples, see the section on Including Data Files.
    # You do not need to use this option if you are using include_package_data, unless you need to add e.g.
    # files that are generated by your setup script and build process. (And are therefore not in source control or are files that you don’t want to include in your source distribution.)
    package_data={
        'custom_search': [  # 包名(应与pybind11定义的python模块名相同,c++源码见:./custom_search.cpp)
            # pybind11 + cmake生成的动态库文件
            'custom_search.cpython-311-x86_64-linux-gnu.so'
        ]
    }
)