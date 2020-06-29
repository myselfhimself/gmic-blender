"""
Prints the latest available gmic-py version from PyPI.org on standard output
This comes in handy for Github CI scripts steps labels.
"""

import yolk.pypi
PYPI_GMIC_PACKAGE_NAME="gmic"

if __name__ == "__main__":
    releases = yolk.pypi.CheeseShop().package_releases(PYPI_GMIC_PACKAGE_NAME)
    releases.sort()
    print(releases[-1], end='')
