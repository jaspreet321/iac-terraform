#So, the CIDR block "10.0.0.0/16" defines a network range from 10.0.0.0 to 10.0.255.255

#The tags attribute is set to a map (key-value pairs), where the key is "Name" and the value is "main". This means that the VPC being created will have a tag with the key "Name" and the value "main". This tag can be useful for identifying the purpose or owner of the VPC.



resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "vpcThroughTerraform"
  }
}
