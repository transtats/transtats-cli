[![Build Status](https://travis-ci.org/transtats/transtats-cli.svg?branch=devel)](https://travis-ci.org/transtats/transtats-cli)

# transtats-cli
Transtats command line interface to query transtats server.

`transtats.conf` should be placed inside `~/.config/` directory.

```shell
Usage: transtats [OPTIONS] COMMAND [ARGS]...

  Transtats CLI to communicate with server

Options:
  --help  Show this message and exit.

Commands:
  coverage  Translation coverage as per graph rule.
  package   Translation status of a package.
  release   Translation status of a release branch.
  version   Display the current version.
```


#### Contribution

* Fork [transtats-cli repo](https://github.com/transtats/transtats-cli) to your username and clone repository locally.
* Setup development environment `pip install -r requirements.txt`
* The *devel* branch is the release actively under development.
* The *master* branch corresponds to the latest stable release.
* If you find any bug/issue or got an idea, open a [github issue](https://github.com/transtats/transtats-cli/issues/new).
* [travis](https://travis-ci.org/transtats/transtats-cli) runs flake8 and tests `python setup.py flake8 test`
* Feel free to submit feature requests and/or bug fixes on *devel* branch.

### License

[Apache License](http://www.apache.org/licenses/LICENSE-2.0), Version 2.0
