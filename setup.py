#!/usr/bin/env python3

# +------------------------+			   
# | Created with Sailboat  |			   
# |			                   |			   
# | Do not edit this file  |			   
# | directly. Instead  	   |			   
# | you should edit the	   |			   
# | `sailboat.toml` file.  |			   
# +------------------------+	

import setuptools

try:
  with open("README.md", "r") as fh:
	  long_description = fh.read()
except:
	long_description = "# Hello_World\n\n### Contributors\n- Cole Wilson\n### Contact\n<cole@colewilson.xyz> "

options = {
	"name":"helloworld_colewilson4",
	"version":"0.0.1",
	"scripts":['bin/hello'],
	"entry_points":{'console_scripts': []},
	"author":"Cole Wilson",
	"author_email":"cole@colewilson.xyz",
	"description":"",
	"long_description":long_description,
	"long_description_content_type":"text/markdown",
	"url":"https://google.com",
	"packages":setuptools.find_packages(),
	"install_requires":[],
	"classifiers":["Programming Language :: Python :: 3"],
	"python_requires":'>=3.6',
	"package_data":{"": [],},
	"license":"none",
	"keywords":'',
}

custom_options = {}

if __name__=="__main__":
	setuptools.setup(**custom_options,**options)