from distutils.core import setup
with open("ALLINONE.md", "r") as f:
    readme = f.read()
setup(
    name="finnsflask",
    packages=['finnsflask'],
    version='1.2',
    license="MIT",
    description='This is a recreation of the popular python package, Flask.',
    author='Real Finnventor',
    author_email='finnventor@everspaugh.com',
    url='https://github.com/the-real-finnventor/finnsflask',
    download_url='https://github.com/the-real-finnventor/finnsflask/archive/refs/tags/1.1.tar.gz',
    keywords=['FLASK', 'WEBSERVER', "JINJA2"],
    install_requires=[
        'Jinja2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    long_description=readme,
    long_description_content_type='text/markdown'
)
