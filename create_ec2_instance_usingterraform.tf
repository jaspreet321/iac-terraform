#this is a script which will create ec2 instance in your aws connect
#this script will only take your input which you provided, for other things like - securitugruops, ip-address, vpc, subnet, route53 terraform will take default values
#these terraform scripts can be referred at https://registry.terraform.io/providers/hashicorp/aws/latest/docs

resource "aws_instance" "server1" {
  ami           = "ami-079db87dc4c10ac91"
  instance_type = "t2.micro"

  tags = {
    Name = "terraform first server"
  }
}

resource "aws_instance" "server2" {
  ami           = "ami-079db87dc4c10ac91"
  instance_type = "t2.micro"

  tags = {
    Name = "terraform second server"
  }
}
