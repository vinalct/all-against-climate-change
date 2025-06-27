variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "Default region for general GCP resources"
  type        = string
  default     = "us-central1"
}

variable "composer_region" {
  description = "Region for Cloud Composer"
  type        = string
  default     = "us-central1"
}

variable "composer_env_name" {
  description = "Name of your Composer environment"
  type        = string
  default     = "owm-airflow-env"
}

variable "dataset_id" {
  description = "BigQuery dataset ID for weather data"
  type        = string
  default     = "owm_weather"
}

variable "dataset_location" {
  description = "BigQuery dataset location"
  type        = string
  default     = "US"
}