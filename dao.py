#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 by Alejandro Rios
#

import sys, os
import time,datetime
from config import *

# DAO for MySQL

try:
	import MySQLdb as mysql
except ImportError:
	print "Note: you should install python mysql libs"

class Question(object):

        def __init__(self,
			id=None,
			descripcion=None,
			audio=None,
			opciones=[]
			):
		self.id=id
		self.descripcion=descripcion
		self.audio=audio
		self.opciones=opciones

	@staticmethod
	def newFromArray(resultRow):
		opciones=[]
		ops = resultRow[3].split(",")
		for op in ops:
			 opciones.append(str(int(op)))
		return Pregunta(
			id=resultRow[0],
			descripcion=resultRow[1],
			audio=resultRow[2],
			opciones=opciones,
			)

	def getId(self):
		return self.id

	def getDescripcion(self):
		return self.descripcion

	def getAudio(self):
		return self.audio

	def getOpciones(self):
		return self.opciones


class DAO(object):

        def __init__(self):
		self.connected=False
		self.db = None

	## Conectar a bd 
        def connect(self):
		try:
			self.db = mysql.connect(host = DBHOST, db = DBNAME, user = DBUSER, passwd = DBPASSWD)
		#	db3.isolation_level = None
			self.connected=True
		except:
			print "Note: you don't seem to have access to mysql. %s" % DBHOST
			if __name__ == "__main__": sys.exit(0)

        def ping(self):
		try:
			if not self.db.ping():
				return True
		except:
			print "Connection to mysql lost. %s" % DBHOST
			return False

	
	def getPreguntas(self):
		cursor = self.db.cursor()

		sql = "SELECT * \
			from pregunta"

		cursor.execute(sql)
		results = cursor.fetchall()
		preguntas = []
		for resultRow in results:
			p = Pregunta.newFromArray(resultRow)
			preguntas.append(p)
		return preguntas

	def addRespuesta(self, recordID=None, callerid=None, id_pregunta=None, respuesta=None):
		if (id_pregunta==0 or recordID==0):
			return False
		cursor = self.db.cursor()
		# Insertar entrada 
		sql = """INSERT INTO respuesta VALUES (NULL,NOW(),'%s',%s,'%s','%s')""" % (recordID,id_pregunta,callerid,respuesta)
		cursor.execute(sql)
		self.db.commit()
		return True


	def record_event(self, recordID=None, evento=None):
		cursor = self.db.cursor()
		# Insertar entrada 
		sql = """INSERT INTO evento VALUES (NULL,NOW(),'%s','%s')""" % (recordID,evento)
		cursor.execute(sql)
		self.db.commit()

if __name__ == "__main__":
	s = DAO()
	s.connect()
	#print s.ping()
	#s.db.close()
	#print s.ping()

	if s.connected:
		print "TEST 1. getPreguntas()"
		pregs = s.getPreguntas()
		print len(pregs)
		print pregs[0].getOpciones()

		print "TEST 2. addRespuesta()"
		print s.addRespuesta("test-123456", "123456", pregs[0].getId(), '3')

	else:
		print "Not connected"
