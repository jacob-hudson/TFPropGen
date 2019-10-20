provider "aws" {
  region 	= "us-east-2"
}
 
resource "aws_instance" "example" {
 
  ami       	= "ami-0c09927662c939f41"
  instance_type = var.terraform_ec2_instance_type
 
  tags = {
	name = var.terraform_ec2_instance_name
  }
}