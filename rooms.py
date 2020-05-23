from bottle import run, get, post, request, delete


@get('/room')
def getAll():
	return {'rooms' : rooms}

@get('/room/<Id>')
def getOne(Id):
	the_room = [room for room in rooms if room['Id'] == Id]
	return {'room' : the_room[0]}

@post('/room')
def addOne():
	new_room = {'Id' : request.json.get('Id'), 'NumPlaz' : request.json.get('NumPlaz')}
	rooms.append(rooms)
	return {'rooms' : rooms}

@delete('/room/<Id>')
def removeOne(Id):
	the_room = [room for room in rooms if room['Id'] == Id]
	rooms.remove(the_room[0])
	return {'rooms' : rooms}

	print("jeje")


run(reloader=True, debug=True)