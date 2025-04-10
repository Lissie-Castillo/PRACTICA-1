from flask import Flask #importamos flask 

app= Flask(__name__) #SE crea una instancia

@app.route("/") #Se crea la url 

def saludo(): # se define ña variable original 
    return " HOLAAA BIENVENIDO AL SEMESTRE"
    
