resource "google_storage_bucket" "backup_bucket" {
    name = "epam-interview-bucket-2024"
    location = "US"
    lifecycle {
        prevent_destroy = true
    }
}