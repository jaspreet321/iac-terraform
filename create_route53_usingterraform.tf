#in simple terms ROUTE53 is mainly to hold the hosted application i.e.,sample123.com
#hostedZone is very important in route53.
#hosted zone holds the dns of the application.
#hostezone acts as an container in route53 & hosted zone is mandatory

#below scripts is simple and says to create an private hostedzone for sample123.com under vpc which you created earlier


resource "aws_route53_zone" "private" {
  name = "sample123.com"

  vpc {
    vpc_id = "vpc-0ddcad718ca84658d"
  }
}
