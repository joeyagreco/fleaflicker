import setuptools

pkg_vars = dict()
with open("fleaflicker/_version.py") as f:
    exec(f.read(), pkg_vars)

package_version = pkg_vars["__version__"]
minimum_python_version_required = pkg_vars["__version_minimum_python__"]

with open("requirements.txt", "r", encoding="utf8") as reqs:
    required_packages = reqs.read().splitlines()

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name="fleaflicker",
    version=package_version,
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="A Python wrapper for the Fleaflicker API.",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="MIT",
    url="https://github.com/joeyagreco/fleaflicker",
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=required_packages,
    python_requires=f">={minimum_python_version_required}",
    keywords="fleaflicker api wrapper api-wrapper fantasy"
)
