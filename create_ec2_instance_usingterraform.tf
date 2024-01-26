#this is a script which will create ec2 instance in your aws connect
#this script will only take your input which you provided, for other things like - security-group, ip-address, vpc, subnet, route53 terraform will take default values
#these terraform scripts can be referred at https://registry.terraform.io/providers/hashicorp/aws/latest/docs


resource "aws_instance" "server1" {
  ami           = "ami-062a49a8152e4c031"
  instance_type = "t2.micro"
  subnet_id     = "subnet-00db483df53807737"  # Specify the subnet ID within your VPC

  tags = {
    Name = "terraform first server"
  }
}

resource "aws_instance" "server2" {
  ami           = "ami-062a49a8152e4c031"
  instance_type = "t2.micro"
  subnet_id     = "subnet-00db483df53807737"

  tags = {
    Name = "terraform second server"
  }
}
