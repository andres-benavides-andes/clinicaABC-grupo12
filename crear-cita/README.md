Deploy Crear Cita

gcloud builds submit --tag gcr.io/miso-arquitectura-325522/crear-cita:latest

gcloud run deploy crear-cita --image gcr.io/miso-arquitectura-325522/crear-cita:latest