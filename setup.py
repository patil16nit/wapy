from distutils.core import setup
setup(
  name = 'wapy',
  packages = ['wapy'],
  version = '0.1.0',
  description = 'A python wrapper for the Walmart Open API',
  author = 'Carlos Roso',
  author_email = 'ce.roso398@gmail.com',
  url = 'https://github.com/caroso1222/wapy',
  download_url = 'https://github.com/caroso1222/wapy/tarball/0.1.0',
  keywords = ['walmart', 'wrapper', 'walmart api', 'api', 'python client', 'python'],
  install_requires=["requests"],
  classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
)
