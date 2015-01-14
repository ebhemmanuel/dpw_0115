class Page:
	def __init__(self):
		self.title = "Bob's Beer"
		self.css = "css/style.css"
		self.head = """
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="UTF-8">
				<link href="{self.css}" rel="stylesheet" type="text/css"/>
				<title>{self.title}</title>
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