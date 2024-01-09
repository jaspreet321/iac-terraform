#this s a short script will connect terraform to aws using the access key that you will enter
#these terraform scripts can be referred at https://registry.terraform.io/providers/hashicorp/aws/latest/docs

provider "aws" {
  region     = "eu-west-1"
  access_key = "AKIAVLRWBG7FT******"
  secret_key = "3HlpwsaHnbb53I614JdMh********"
}
