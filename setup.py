from setuptools import setup, find_packages

setup(
    name='pitagentsai',
    version='1.1.0',
    description='A professional and scalable Flask-based Agent Framework with blockchain-like token management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='PIT Agent',
    author_email='dev@pitagentai.com',
    url='https://github.com/pitagentsai/pitagents',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.3.2',
        'Flask-SQLAlchemy>=3.0.5',
    ],
    entry_points={
        'console_scripts': [
            'agent-framework=app:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    keywords='flask, agent, blockchain, token management, framework',
    license='MIT',
)
