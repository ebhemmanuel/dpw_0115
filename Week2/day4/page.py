class Page:
	def __init__(self):
		self.title = "Bob's Beer"
		self.css = "css/main.css"
		self.description = "Base File"
		self.head = """
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="utf-8">
		    <meta description="{self.description}">
		    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
		    <link href="css/bootstrap.min.css" type="text/css" rel="stylesheet">
		    <link href="css/bootstrap-theme.min.css" type="text/css" rel="stylesheet">
		    <link href="{self.css}" type="text/css" rel="stylesheet">
			</head>
			<body>
		"""

		self.body = """
			Welcome to OOP
		"""
		self.close = """
			</body>
		</html>
		"""
	def printOut(self):
		html = self.head + self.body + self.close
		html = html.format(**locals()) # Allows for local variables to used using {}
		return html