MADROB-BEAST Performance Indicators
=================================================

Scripts to calculate performance indicators for the MADROB and BEAST benchmarks, from the Eurobench project.

## Installing the library

Pip can be used to install this module locally:

```term
git clone https://github.com/madrob-beast/madrob_beast_pi.git
cd madrob_beast_pi
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -e src/madrob_beast_pi
```

Using the virtual environment, the package and dependencies is installed locally in the folder `venv`.
To deactivate the virtual environment, type `deactivate`.

To install permanently the code, only use the last command.

**Note**: When adding or modifying Performance Indicators, run the installation command again.
To keep the PIs up-to-date, run `git pull` and the installation command.

## Usage

All PI associated to madrob can be launched using (assuming folder `out_tests` exists):

```term
run_madrob tests/madrob/input/events.csv tests/madrob/input/wrench.csv tests/madrob/input/jointState.csv tests/madrob/input/testbed_config.yaml out_tests
```

All PI associated to beast can be launched using (assuming folder `out_tests` exists):

```term
run_beast tests/madrob/input/wrench.csv tests/madrob/input/testbed_config.yaml out_tests
```

<!-- TODO update beast -->

## Build docker image

The Dockerfile in this project can be used to build Docker images for madrob and beast:

### Madrob
```term
docker build -t=pi_madrob .
```

### Beast
```term
docker build -t=pi_beast .
```

## Launch the docker image

### Madrob
Assuming the tests/madrob/input contains the input data, the PI output will be written to out_tests:

```term
docker run --rm -v $PWD/tests/madrob/input:/in -v $PWD/out_tests:/out pi_madrob run_madrob /in/events.csv /in/wrench.csv /in/jointState.csv /in/testbed_config.yaml /out
```

### Beast
Assuming the tests/beast/input contains the input data, the PI output will be written to out_tests:

```term
docker run --rm -v $PWD/tests/beast/input:/in -v $PWD/out_tests:/out pi_beast run_beast /in/wrench.csv /out
```

<!-- TODO update beast -->

## Test data

The [tests/madrob/input](tests/madrob/input) directory contains preprocessed `.csv` files and a testbed configuration `.yaml` file.
The [tests/madrob/output](tests/madrob/output) directory contains the pi output `.yaml` file.
These files are from a real benchmark run, and can be used to test the `run_pi` command and Docker images.

Beast data is not available yet.
<!-- TODO update beast -->

## Acknowledgements

<a href="http://eurobench2020.eu">
  <img src="http://eurobench2020.eu/wp-content/uploads/2018/06/cropped-logoweb.png"
       alt="rosin_logo" height="60" >
</a>

Supported by Eurobench - the European robotic platform for bipedal locomotion benchmarking.
More information: [Eurobench website][eurobench_website]

<img src="http://eurobench2020.eu/wp-content/uploads/2018/02/euflag.png"
     alt="eu_flag" width="100" align="left" >

This project has received funding from the European Union’s Horizon 2020
research and innovation programme under grant agreement no. 779963.

The opinions and arguments expressed reflect only the author‘s view and
reflect in no way the European Commission‘s opinions.
The European Commission is not responsible for any use that may be made
of the information it contains.

[eurobench_logo]: http://eurobench2020.eu/wp-content/uploads/2018/06/cropped-logoweb.png
[eurobench_website]: http://eurobench2020.eu "Go to website"
