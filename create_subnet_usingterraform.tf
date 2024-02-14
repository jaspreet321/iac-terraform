#A subnet is a portion of a network that shares a common IP address prefix
#It divides a larger network into smaller, more manageable parts.

#In simple terms, consider vpc as big buscuit and subnet's are smaller pieces of the same biscuit. 
#This is done in order to divide network in smaller chunks, so that it's easy to manage it.


resource "aws_subnet" "main" {
  vpc_id     = "vpc-0ddcad718ca84658d"
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Main"
  }
}
