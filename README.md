# k-POD: A Method for k-Means Clustering of Missing Data

The k-means algorithm is often used in clustering applications but its usage requires a complete data matrix. Missing data, however, are common in many applications. Mainstream approaches to clustering missing data reduce the missing data problem to a complete data formulation through either deletion or imputation but these solutions may incur significant costs. The k-POD method presents a simple extension of k-means clustering for missing data that works even when the missingness mechanism is unknown, when external information is unavailable, and when there is significant missingness in the data.

## Getting Started

These instructions will walk you through the process of installing and using the k-POD package in your local environment.

### Prerequisites

First, ensure that you have the package manager ```pip``` installed for your Python version. You can find the installation instructions at <a href="https://pip.pypa.io/en/stable/installing/">this link.</a>

In order to use k-POD, you should have <a href="https://pandas.pydata.org/getting_started.html">Pandas</a>, <a href="https://scipy.org/install.html">NumPy</a>, and <a href="https://scipy.org/install.html">SciPy</a> Installation instructions can be found in the links shown or below in the examples. 

```
# install Pandas
pip install pandas

# install NumPy
pip install numpy

# install SciPy
pip install scipy
```

### Installation

The k-POD Python package was designed simplistically and the installation can be accomplished in only one step, assuming the dependencies mentioned above are installed.

Use the package manager pip (installation instructions above) to install the k-POD package.

```
pip install kpod
```

That's it! You should now have k-POD installed locally on your device.

## Usage

---To be Implemented---

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

Take some kind of public dataset to demonstrate k-POD.

Describe the value added. 

## Examples

---To be Implemented---

## Citation

This package was implemented based on the algorithm and concepts in [k-POD](https://www.tandfonline.com/doi/abs/10.1080/00031305.2015.1086685), a research publication describing an extension of k-means clustering to missing data.

## Authors

* **Ishaan Radia** - *Translated paper to Python package, responsible for maintenance of package.* - [GitHub](https://github.com/iiradia)

* **Jocelyn T. Chi** - *Co-Author of k-POD paper and algorithm.* - [Website](https://jocelynchi.com/)

* **Eric C. Chi** - *Co-Author of k-POD paper and algorithm.* - [Website](http://www.ericchi.com/)

* **Richard G. Baraniuk** - *Co-Author of k-POD paper and algorithm.* - [Website](https://richb.rice.edu/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License. You can find more details in the [LICENSE.md](https://github.com/iiradia/kPOD/LICENSE.md) file.
