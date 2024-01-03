#this is a  script where terraform itself download the plugin to connect to aws 
#terraform init command will check for below script in the repository
#these terraform scripts can be referred at https://registry.terraform.io/providers/hashicorp/aws/latest/docs

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}
