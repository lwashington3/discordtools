from setuptools import setup


with open("README.md", 'r') as f:
	long_description = f.read()


project_name = "discordtools"
git_url = f"https://github.com/lwashington3/{project_name}"


setup(
	name=project_name,
	version="1.0.2",
	author="Len Washington III",
	description="Discord Bot Tools",
	include_package_data=True,
	long_description=long_description,
	long_description_content_type="test/markdown",
	url=git_url,
	project_urls={
		"Bug Tracker": f"{git_url}/issues"
	},
	license="MIT",
	packages=[project_name],
	install_requires=["discord-py-interactions"],
	entry_points={
		"console_scripts": [f"{project_name}={project_name}.command_line:main"]
	},
	classifiers=[
		"Programming Language :: Python :: 3.10"
	]
)
