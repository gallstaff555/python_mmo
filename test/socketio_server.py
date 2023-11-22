import socketio
import eventlet

# Create a Socket.IO server
sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')

# Create a WSGI application
app = socketio.WSGIApp(sio)

# Define a Socket.IO event for when a client connects
@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

# Define a Socket.IO event for when a client disconnects
@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)

# Run the application using Eventlet
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
