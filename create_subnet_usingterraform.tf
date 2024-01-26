resource "aws_subnet" "main" {
  vpc_id     = "vpc-0a4e9a524da70c843"
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Main"
  }
}
