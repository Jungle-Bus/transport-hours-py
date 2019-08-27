# Transport Hours (Python version)

## Read-me

TransportHours is a Python (2.7+) library for easy reading/writing of [public transport hours](https://wiki.openstreetmap.org/wiki/Key:interval) present in OpenStreetMap. It interprets string values from OSM tags, and also converts your objects into string values to go back into OSM.


## Install

### From pip

TODO

### Using this repository

Download this repository, then embed the library into your own project :

```python
from transporthours.main import Main
```


## Usage

An example of usage is available in [example.py](example.py) file.

For more details about available functions, see [API documentation](API.md).


## Build & develop

For start developing on this library, run the following commands :

```bash
# Prepare python 2.7 environment
virtualenv env -p /usr/bin/python2.7
source ./env/bin/activate

# Install dependencies
make deps

# Run unit tests
make test

# Generate documentation
make docs
```


## License

Copyright 2019 Jungle Bus & [Adrien PAVIE](https://pavie.info/)

See [LICENSE](LICENSE) for complete LGPL3 license.

TransportHoursPython is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TransportHoursPython is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with TransportHoursPython. If not, see <http://www.gnu.org/licenses/>.
