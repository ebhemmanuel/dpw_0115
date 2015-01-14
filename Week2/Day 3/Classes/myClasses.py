#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# import webapp2
# from views import Page


# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         p = Page()
#         #send in the content we need
#         # print out the content we want
#         p.content = "Sign the form below:"
#         p.css = "css/application.css"
#         self.response.write(p.print_out())


        # instance = Class()
#         yoda = Character() #create instance
#         yoda.name = "Jedi Master"
#         yoda.occupation = "Jedi Knight"
#         yoda.hometown = "Dagoba"
#         yoda.age = 900
#         yoda.quote = "You're my only hope!"
#         self.response.write(yoda.fight())
#
#
#         leia = Character()
#         leia.name = "Princess Leia Organa"
#         leia.occupation = "Princess, General of Rebel Forces"
#         leia.hometown = "Alderaan"
#         leia.age = 12
#         leia.quote = "You're my only hope!"
#         self.response.write(leia.say())

class Player(object):
	def __init__(self):
		# print "Player created"
		self.name = "player"
		self.color = "Red"
		self.movement = 2.5
		self.speed = 1
		self.alive = 1
		def eat(self):
			print "waka"

class Ghost(object):
	def __init__(self):
		self.name = "Boom"
		self.speed = 2
		self.ai = 1
		self.alive = 1
		self.status = "Idle"
		def die(self):
			print "Return to home"
# A constructor function runs when you instantiate the object
# For example:
# instance = Class()
# pacMan = Player()
# pacMan.color = "Yellow"
# print pacMan.name
# Looping through an array of players
# players = []

# for i in range(1,101,1):
# 	players.append(Player())

# for i in players:
# 	print i.name

# class Car(object):
# 	def __init__(self):
			# self.door = 0
			# self.make = " "
			# self.modle = " "
			# self.working = True
			# self.automatic = True

class Car:
	def __init__(self,make):
		print "Car Created"
		self.door = 0
		self.make = " "
		self.model = " "
		self.working = True
		self.automatic = True
	def start(self):
		if self.working == True:
			print "My " + self.make + " is working."
		else:
			print "My " + self.make + " is a pos."

# myCar = Car()
# myCar.make = "Toyota"
# myCar.start()
# myCar = Car("Toyota")
# myCar.working = False
# myCar.start()


#
# class file is a set of directions
# or a blueprint
# class Character(object):
#     def __init__(self):
#         self.name = " "
#         self.occupation = ' '
#         self.age = 0
#         self.hometown = ' '
#
#     def fight(self):
#         print "Don't you dare lay a hand on my butterfinger!"
#
#     def say(self):
#         print self.hometown
#         return self.quote

# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)
