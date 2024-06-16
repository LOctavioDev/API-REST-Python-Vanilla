from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #Verificar si la ruta es "/""
        if self.path == '/':
            #Verificar que el codigo de estado de la respuesta sea 200 (Ok)
            self.send_response(200)

            #Establecer el tipo de contenido de la respuesta a 'application/json'
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            #Crear la respuesta con el mensaje JSON
            response = {'message' : 'Hola desde: Python', 'framework': False}
            
            #Enviar la respuesta con el mensaje JSON
            self.wfile.write(json.dumps(response).encode())
        else:
            #Si la ruta no es "/", responder con un 404 (Not Found)
            self.send_response(404)
            self.end_headers()     
             
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
        #Definir la direccion y el puerto donde el servidor escuchara
        server_address = ('', 3000)
        
        #Creamos una instancia del servidor
        httpd = server_class(server_address, handler_class)
        
        #Imprimir un mensaje indicando que el servidor esta corriendo
        print('SERVER RUNNING ON: http://localhost:3000')
        
        #Poner el servidor a escuchar
        httpd.serve_forever()
        

if __name__ == '__main__':
    run()