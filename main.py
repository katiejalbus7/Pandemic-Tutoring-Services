import posts
import webapp2

class MainPageHandler(webapp2.RequestHandler):
	get(self): self.responsewrite(posts.MAINPAGE)
	
class VolunteersHandler(webapp2.RequestHandler):
	get(self): self.responsewrite(posts.VOLUNTEER)
	