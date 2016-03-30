import webapp2 
import os
import logging
import jinja2

#http://www.jinja2templates5.appspot.com

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	try:
    		template = JINJA_ENVIRONMENT.get_template('templates%s' % self.request.path)
    		title_name = "Welcome to the %s" % self.request.path.strip('/.html')
    		self.response.write(template.render({'title':title_name}))
    		#page_name = self.request.path.strip('/.html')
    		#logging.info(page_name)
    		#self.response.write(template.render({'pagename':page_name}, {'title':title_name}))
    	except:
    		template = JINJA_ENVIRONMENT.get_template('templates/aboutus.html')
    		self.response.write(template.render({'title':'Welcome to the Home page'}))

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/login.html')
		self.response.write(template.render({'title':'Welcome to the Login page'}))
	def post(self):
		template = JINJA_ENVIRONMENT.get_template('templates/login.html')
		user_name = self.request.get('name')
		pass_word = self.request.get('pw')
		if (user_name == "Colleen") and (pass_word == "pass"):
			template = JINJA_ENVIRONMENT.get_template('templates/logincorrect.html')
			self.response.write(template.render({'title':'Logged in'}))
		else:
			message = "Bad credentials. Try again."
			logging.info("Entered username is: %s" % user_name)
			logging.info("Entered password is: %s" % pass_word)
			template = JINJA_ENVIRONMENT.get_template('templates/login.html')
			self.response.write(template.render({'msg':message, 'title':'Welcome to the Login page'}))
			

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/aboutus.html', MainHandler),
    ('/meettheboards.html', MainHandler),
    ('/previousconference.html', MainHandler),
    ('/currentconference.html', MainHandler),
    ('/knowoursponsors.html', MainHandler),
    ('/login.html', LoginHandler),
    ('/logincorrect.html', LoginHandler)
], debug=True)
