# Sample Package Structure

Packaging and building seems to be an evolving thing in Python world.
Here's what I found so far that I like:

	* use pyproject.toml as much as possible, it seems to have replaced setup.cfg
	* still using pip as a package manager.
	* started using 'hatchling' as a build tool (since setuptools required distutils which
	  is slowly being deprecated.)
	* keep tests isolated from other packages
	  * but then test code has to reference the src.package-name path.
	* use pytest as a replacement for unittest
	* use pytest-cov for coverage
	* use sphinx for documentation (use sphinx-quickstart in docs to setup)
	