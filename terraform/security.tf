resource "aws_security_group" "api" {
  name        = "${var.project_name}-api-sg"
  description = "Security group for the CloudOps Platform API"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "Allow HTTP API traffic from the VPC"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    description = "Allow outbound IPv4 traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "${var.project_name}-api-sg"
    Environment = "development"
    ManagedBy   = "Terraform"
  }
}
