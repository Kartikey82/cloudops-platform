output "vpc_cidr_block" {
  description = "CIDR range planned for the project VPC"
  value       = aws_vpc.main.cidr_block
}

output "vpc_id" {
  description = "ID of the project VPC after deployment"
  value       = aws_vpc.main.id
}
