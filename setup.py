from distutils.core import setup

setup(
    name='TinyASGI',
    version='0.1',
    description='Based on starlette',
    author='Arty',
    author_email='artythedev@gmail.com',
    url='https://github.com/ArtyTheDev/tinyasgi',
    packages=[
        "tinyasgi",
        "tinyasgi.wrappers",
    ],
    install_requires=[
        "starlette", "asgiref"
    ],
    python_requires=">=3.6",
    platforms="any",
)