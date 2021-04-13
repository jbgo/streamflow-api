Streamflow API
==============

Real-time stream data, analytics, and predictions.

System Requirements
-------------------

* Python 3.7+
* Pip (latest)
* MySQL 5.7+

Development Setup
-----------------

Setup instructions for Debian-based distros.

    sudo apt-get install -y python3 python3-pip
    git clone ...
    cd ...
    python3 -mvenv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

### Configuration

All configuration is performed through environment variables. The provided
`Makefile` assumes you have both a `.env` and `.env.test` in the top-level
project directory. The provided `.env.example` describes each variable and
can be used as a template to create your personal `.env` and `.env.test` files.
Both `.env` and `.env.test` are excluded in `.gitignore` to avoid accidentally
commiting secrets to the git repo.


### Testing

Tests are written with [pytest](https://docs.pytest.org/en/stable/) and located
in the `test/` directory. Once you complete the Development Setup and
Configuration steps, you can run tests with

    make

### Running

You can run a local development server with

    make serve
