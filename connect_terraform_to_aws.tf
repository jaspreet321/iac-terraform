#this s a short script will connect terraform to aws using the access key that you will enter
#these terraform scripts can be referred at https://registry.terraform.io/providers/hashicorp/aws/latest/docs

provider "aws" {
  region     = "eu-west-1"
  access_key = "AKIAVLRWBG7FZ74DOYDH"
  secret_key = "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"
}
