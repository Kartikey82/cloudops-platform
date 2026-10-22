variable "aws_region" {
  description = "AWS region for the CloudOps Platform infrastructure"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Name used to identify project resources"
  type        = string
  default     = "cloudops-platform"
}
