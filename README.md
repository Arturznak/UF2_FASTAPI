# UF2_FASTAPI

## Funció GET SWAGGER
![](ACTIVITAT_8/Imatges/Swaggerget.png)
El resultat ens mostra que l'item id es 1 que es el que hem escrit a description, com hem declarat que item_id sigui un int al rebre-ho ens ho retorna igual.

## Funció GET POSTMAN
![](ACTIVITAT_8/Imatges/Postmanget.png)
Igual ens pasa a Postman, com a la url al final posem un número, l'item_id al ser int ens retorna el que rep.

## Funció POST SWAGGER
![](ACTIVITAT_8/Imatges/SwaggerPost1.png)
![](ACTIVITAT_8/Imatges/SwaggerPost2.png)
El resultat a Post amb el model de dades sortiría l'informació proporcionada al request body i al deixar la "descripció" com a opcional i no posar cap valor, al response body surt com a null.

## Funció POST POSTMAN
![](ACTIVITAT_8/Imatges/PostmanPost.png)
A Postman es pot veure el matexi resultat.

## Funció GET(response) SWAGGER
![](ACTIVITAT_8/Imatges/SwaggerResponse.png)
![](ACTIVITAT_8/Imatges/SwaggerResponse1.png)
Al resultat es pot veure com el response funciona correctament ja que ens retorna el status code a responses.

## Funció GET(response) POSTMAN
![](ACTIVITAT_8/Imatges/PostmanResponse.png)
Igual ens pasa a Postman on podem veure que funciona correctament perque ens surt el 201 created o sigui el status code.

## Funció GET(HTTPException) SWAGGER
![](ACTIVITAT_8/Imatges/SwaggerHttpException.png)
El resultat del item quan posem el 9 és "número nou" ja que es la dada que tenim emmagatzemada a items.

![](ACTIVITAT_8/Imatges/SwaggerHttpException2.png)
En canvi si posem qualsevol altre número com el 7 ens surt item no trobat, ja que com no troba aquest número a items ens llença l'excepció amb el missatge.

## Funció GET(HTTPException) POSTMAN
![](ACTIVITAT_8/Imatges/PostmanHttpException.png)
A Postman podem veure el mateix resultat.

![](ACTIVITAT_8/Imatges/PostmanHttpException2ç.png)
A Postman podem veure el mateix resultat.