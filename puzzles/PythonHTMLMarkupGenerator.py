# Generate an HTML file with user input for title and the content of a single paragraph

import webbrowser


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
        webbrowser.open("result.html")

if __name__ == '__main__':
    gen_html_file('This is a test', title='Test page', open_output=True)
