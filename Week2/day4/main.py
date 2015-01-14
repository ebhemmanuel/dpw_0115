import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
			p      = Page()
			p.body = "Yay"
			html   = p.printOut()
			self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
