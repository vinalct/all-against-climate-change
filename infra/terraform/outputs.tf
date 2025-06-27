output "composer_environment_name" {
  description = "Composer environment ID"
  value       = google_composer_environment.airflow.name
}

output "composer_airflow_uri" {
  description = "Airflow web UI endpoint"
  value       = google_composer_environment.airflow.config.0.airflow_uri
}

output "bigquery_dataset_id" {
  description = "BigQuery dataset for weather data"
  value       = google_bigquery_dataset.weather.dataset_id
}