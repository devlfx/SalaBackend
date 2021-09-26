# SalaBackend
Backend for the project "Sala de Espera Virtual" (SEVi)

## Disclaimer
This project was made with academical purposes and should be taken as that. It's and MVP and should not be used in production.

## Description
This project was born to help people in Mexico with hospital emergencies in times of pandemic (2019 - x)
it aims to keep the relatives of a hospitalized patient informed, without having to stop them in their daily activities.

So when there is information available this backend will send the information using push notifications for the relative, right now only supports
Apple Notifications. Maybe in a future android and email notifications will be integrated.

## Technologies
 - Python
 - FastAPI
 - Heroku (for deployment)
 - uvicorn (Server)
 - Postgres (DB)
 

## Libraries
 - fastAPI
 - passlib
 - psycopg2-binary
 - fastapi-jwt-auth
 - python-decouple
 - SQLAlchemy
 - HTTPX

## Documentation 

The documentation for this project can be found here:
 	[Documentation](https://salaesperavirtual.herokuapp.com/docs)
  
  
  
## Todo
 - Implement notifications when a procedure is authorized.
 - Allow to share the care with userd via some QR Code.
 - Send notifications When the patient is ready to have visits.
 - Create the neccesary procedure for implementing this on a real hospital
 - Many things more...
