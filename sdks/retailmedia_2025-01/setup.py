# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "criteo-api-retailmedia-sdk"
VERSION = "2025.01.0.250709"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "python-dateutil"]

AUTHOR='Criteo'
README_CONTENT_TYPE='text/markdown'
PACKAGE_LONG_DESCRIPTION = """# Criteo API SDK for Python

IMPORTANT: This Python package links to Criteo production environment. Any test applied here will thus impact real data.

## Installation & Usage
### pip install


```sh
pip install criteo-api-retailmedia-sdk==2025.01.0.250709
```
(you may need to run `pip` with root permission: `sudo pip install criteo-api-retailmedia-sdk==2025.01.0.250709`)

Then import the package:
```python
import criteo_api_retailmedia_v2025_01
```

Full documentation on [Github](https://github.com/criteo/criteo-api-python-sdk).

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

setup(
    name=NAME,
    version=VERSION,
    description="Criteo API SDK",
    author_email="",
    author=AUTHOR,
    url="https://github.com/criteo/criteo-api-python-sdk",
    keywords=[AUTHOR, "OpenAPI-Generator", "Criteo API SDK"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type=README_CONTENT_TYPE,
    long_description=PACKAGE_LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
