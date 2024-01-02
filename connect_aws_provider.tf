#this s a short script to connect terraform to aws using terraform init command
#terraform init will check for below script in the repository

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}
