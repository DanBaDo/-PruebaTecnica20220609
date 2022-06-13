# PruebaTecnica20220609

## Consultas a la DB

* GET /profiles/: 1
* POST /profiles/: 1
* GET profiles/validate/ 1

## Curl

### GET /profiles/
```bash
curl --request GET \
--url http://127.0.0.1:8000/profiles/
```

### POST /profiles/
```bash
curl --request POST \
  --url http://127.0.0.1:8000/profiles/ \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "qweqw",
    "surname": "qweqwe",
    "email": "qweq@qqweqwe.ws",
    "phone": "+34616656123"
}'
```

### GET profiles/validate/
```bash
curl --request GET \
  --url http://127.0.0.1:8000/profiles/validate/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZGRyZXNzX3ZlcmlmaWNhdGlvbiIsImF1ZCI6ImFkZHJlc3NfdmVyaWZpY2F0aW9uIiwic3ViIjoyMSwidmVyaWZ5X3Byb3BlcnR5IjoicGhvbmUiLCJwcm9wZXJ0eV9zcGVjdGVkX3ZhbHVlIjoiKzM0NjE2NjU2MTIzIn0.E4sHxr0DUFdlR0sU39DaarKeU7BIcSPwWFvpFE3VTuo
```

## Preguntas

* ¿Qué te ha parecido la prueba? ¿Te ha gustado? ¿Te ha parecido sencilla, media,
compleja?
    * El objetivo me parece sencillo, pero ya que en las entrevistas insististeis en la solidez y calidad del código me lie la manta a la cabeza con type hinting, que no acostumbro a usar. Por otra parte, no sabía nada de Django REST, así que me he tenido que pelear con ello. Entre el type hinting y Django REST no voy a decir que no lo haya pasado un poco mal. Eso no quita que no me haya gustado ;-)


* ¿Hay algún punto que te haya parecido confuso de la prueba?
  * No tengo muy claro si quereis que la parte del envío de las confirmaciones de tlf/email sean más reales. Si quereis puedo simular la conexión a alguna API real.

* ¿Has aprendido algo con esta prueba?
  * Cosas de type hinting, de Django REST y async en Python. Es la primera vez que trabajo estas cosas excepto Django REST en otra prueba técnica.

* ¿Cuánto tiempo has tardado en hacer la prueba?
  * Mucho. Unas seis horas, más o menos.

* ¿Qué es lo más divertido que has desarrollado? ¿Qué es lo que más te gusta
desarrollar?
  * Me gusta hacer cosas útiles. Que solucionen problemas. Programar es divertido.

* ¿Qué es lo que más odias desarrollar?
  * ... CSS no es mi mejor amigo.

* ¿Tienes manías desarrollando? ¿Cuáles son?
  * Creo que ninguna mala. Quizá, como en el caso, intentar forzar un poco más de lo que me resulta cómodo, pero es la forma de superarse. 

* ¿Te gustaría comentar algo extra? ¿Te habría gustado que te hiciéramos alguna
pregunta?
  * Pediros disculpas por no incluir tests de intergación para los endpoint. No me puedo permitir dedicarle más tiempo a la prueba en este momento.

* Después de hacer la prueba, ¿tienes algunas dudas extras sobre cómo trabajamos?
  * Las tendré

* ¿Cambiarías algo de la prueba para completarla con algo que consideres
importante?
  * Como os comentaba, dedicaría algún tiempo a tests de integración y han quedado algunos TODO en el código.