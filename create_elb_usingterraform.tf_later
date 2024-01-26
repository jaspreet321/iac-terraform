# Create a new load balancer
resource "aws_elb" "terraform_elb" {
  name               = "terraform-elb"
  availability_zones = ["eu-west-1c"]
  subnet_id          = "subnet-00db483df53807737"  # Specify the subnet ID within your VPC

  access_logs {
    bucket        = "terraform-test-bucket"
    bucket_prefix = "terraformbucket"
    interval      = 60
  }

  listener {
    instance_port     = 8000
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 3
    target              = "HTTP:8000/"
    interval            = 30
  }

  instances                   = ["i-090f002310bc8b50b", "i-0eb395a4acf244a90"]
  cross_zone_load_balancing   = true
  idle_timeout                = 400
  connection_draining         = true
  connection_draining_timeout = 400

  tags = {
    Name = "lbThroughTerraform"
  }
}
