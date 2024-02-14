resource "aws_s3_bucket" "terraform_bucket123" {
  bucket = "terraform-verify-bucket"

  tags = {
    Name        = "terraform_bucket"
  }
}
