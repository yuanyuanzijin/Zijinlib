from setuptools import setup, find_packages
setup(
    name='zijinlib',
    version="0.13.1",
    description=(
        'A package which can make your python programing more convenient.'
    ),
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    author='yuanyuanzijin',
    author_email='yuanyuanzijin@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/yuanyuanzijin/zijinlib',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
