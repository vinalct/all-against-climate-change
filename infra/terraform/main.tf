
resource "google_service_account" "composer" {
  account_id   = "owm-composer-sa"
  display_name = "Service Account for Cloud Composer"
}


resource "google_project_iam_member" "composer_roles" {
  for_each = toset([
    "roles/composer.admin",       
    "roles/storage.admin",       
    "roles/pubsub.editor",       
    "roles/bigquery.dataEditor",  
    "roles/bigquery.jobUser",     
  ])
  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.composer.email}"
}

resource "google_composer_environment" "airflow" {
  provider = google-beta
  name     = var.composer_env_name
  region   = var.composer_region

  config {
    node_count = 3

    software_config {
      image_version = "composer-2.1.0-airflow-2.4.1"
    }

    node_config {
      service_account = google_service_account.composer.email
      machine_type  = "n1-standard-1"
      network       = "default"
    }
  }
}

resource "google_bigquery_dataset" "weather" {
  dataset_id       = var.dataset_id
  project          = var.project_id
  location         = var.dataset_location
  friendly_name    = "OpenWeatherMap Data"
  description      = "Stores raw weather data"
}