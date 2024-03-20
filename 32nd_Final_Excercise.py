#--------------------------------------------------------------------------------------------------------

from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0: 
            return "Positivo"
        elif analisis.sentiment.polarity == 0: 
            return "Neutro"
        else: 
            return "Negativo"

analizer = AnalizadorDeSentimientos()
answer =  analizer.analizar_sentimiento("I'm feeling tired")
print(answer)

#--------------------------------------------------------------------------------------------------------

import openai

open.api_key = ""
system_role = ''' Haz de cuenta que sos un analizador de sentimientos. Yo te paso sentimientos y vos analizar 
el sentimiento de los mensajes y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres SOLO 
RESPUESTAS NUMERICAS. Donde -1 es negatividad máxima, 0 es nutral y 1 es de positividad máxima. Podes ir entre 
esos rangos, es decir 0.3, -0.5 etc también son validos. (Podes responder solo con ints o floats) '''

mensajes = [{"role":"system","content":system_role}]

class Sentimiento:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[1;37m".format(self.color,self.nombre)

class AnalizadorDeSentimientos:
    def  __init__(self,rangos):
        self.rangos = rangos
        
    def analizar_sentimiento:
        for rangos, sentimiento in self.rangos:
            if rango[0] > polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo","31")

rangos = [
            ((-0.6,-0.3), Sentimiento("Negativo","31"))
            ((-0.3,-0.1), Sentimiento("Algo Negativo","31"))
            ((-0.1,0.1), Sentimiento("Neutral","33"))
            ((0.1,0.3), Sentimiento("Algo Positivo","32"))
            ((0.3,0.9), Sentimiento("Positivo","32"))
            ((0.9,1), Sentimiento("Muy Positivo","32"))
        ]

while True:
    user_propmt = input("Demore Algo:")
    mensajes.append({"role":"user","content":user_propmt})

    completion = openai.ChatCompletioncreate(
            model = "gpt-3,5-turbo",
            messages = mensajes,
            max_tokens = 8
            )

    respuesta = completion.choises[0].message['content']
    mensajes.append({"role":"assistant","content":respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)

#--------------------------------------------------------------------------------------------------------
