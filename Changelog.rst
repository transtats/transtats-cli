Changelog
=========

0.6.0 (2022-07-01)
-----------------
- transtats add --package cmd (sdp5)
- Implement add package command (sdp5)
- Extract package commands to a new group for adding new packages
  and showing stats, health etc. (sdp5)
- Update unit tests (sdp5)
- Update man page (pnemade)

0.5.0 (2021-07-12)
-----------------
- Update textoutput.py (sundeep-co-in)
- Add new options repo-type and repo-branch to job run command (sundeep-co-in)
- Update man page (pnemade)
- Change Problematic language in code (pnemade)

0.4.0 (2020-07-09)
-----------------
- Dropping flake8 dependency (pnemade)

0.3.0 (2019-08-02)
-----------------
- Add new options exist and health to package command (pnemade)
- update the man page for package command enhancement (pnemade)
- Added new coverage formats in coverage command (suanand)
- Changed "graph_rule" to "coverage_rule" (pnemade)
- Added validation checks to check if server is responding or not (pnemade)
- Updated test cases to accommodate above changes (pnemade)

0.2.0 (2018-08-04)
-----------------
-  Add partial bash-completion support for job command (pnemade)
-  Test fixes (sundeep-co-in)
-  Added transtats job command.
   Added run and log as subcommands to job command.
   Updated man page. (pnemade)

- Added Makefile for this project (pnemade)
- Added locale option to release command.
  This option is available for text as well as json output.
  Supporting test case also added in this commit. (pnemade)

- Remove trailing slash from the endpoint (sundeep-co-in)
- Added bash completion for transtats commands (pnemade)

0.1.2 (2018-02-27)
-----------------
- Fix the plain text output from the tables by sorting list data - (sundeep-co-in)
- Fix some cosmetic changes in the code - (sundeep-co-in)
- Add plain text output for the transtats commands - #11 (pnemade)

0.1.1 (2017-11-15)
-----------------
- Update endpoints - #8, #9 (sundeep-co-in)
- Add tests - #6 (sundeep-co-in)
- Add config file parsing using configparser - #5 (pnemade)

0.1.0 (2017-09-12)
-----------------
- Basic Commands - #1 (sundeep-co-in)
