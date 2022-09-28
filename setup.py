import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(name='pascals_triangle',
      version = '0.1',
      description = "Object Oriented Pascal's Triangle Library",
      long_description = long_description,
      long_description_content_type = "text/markdown",
      url = 'https://github.com/lukaszp/pascals-triangle.git',
      author = 'Lukasz Paszke',
      author_email = 'lukasz.paszke@gmail.com',
      license = 'MIT',
      packages = setuptools.find_packages(),
      install_requires = [],
      extras_require = {'dev': ['hypothesis']},
      classifiers = ["Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent"],
      python_requires = '>=3.8')
