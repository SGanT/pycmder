# PYCMDER
A tool which executes BASH commands with arguments in directories, specified in JSON file
***
## USAGE
The syntax of Pycmder is simple. Open your terminal, move to a directory, where your file is located and type: **./pycmder.py `PATH_TO_JSON`**, where `PATH_TO_JSON` is a path to JSON file.
***
## JSON file
```JSON
[
	{
		"path": "/path/to/dir",
		"util": "command",
		"args": [
			"argument1",
			"argument2"
		],
		"flags": [
			"--someflag"
		]
	}
]
```
The global array `[]` may contain several `paths` (`{}`). The util you want to run will be executed with each of the arguments separately. That means util `command` will be called twice: with argument `argument1` and then `argument2`. 

**Remember that flags with syntax `--flagname value` are not supported yet** 