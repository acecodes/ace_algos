# Generate an HTML file with user input for title and the content of a single paragraph

from os import system

def gen_html_file(entry, title="Default Title", open_output=False):
	output = """<!DOCTYPE html>
	<html>
	    <head>
	        <title>{title}</title>
	    </head>

	    <body>
	        <p>{entry}</p>
	    </body>
	</html>
	""".format(entry=entry, title=title)

	with open("result.html", 'w') as html_generator:
		html_generator.write(output)

	if open_output == True:
		system("""firefox 'result.html'""")