Deploy Consulta Cita

gcloud builds submit --tag gcr.io/miso-arquitectura-325522/consulta-citas:latest

gcloud run deploy consulta-citas --image gcr.io/miso-arquitectura-325522/consulta-citas:latest