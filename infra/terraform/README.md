# Terraform Skeleton (ECS Task + Logs)

This is a minimal skeleton to illustrate an ECS Fargate task definition and CloudWatch logs. You will need to create VPC, subnets, security groups, ALB, ECS cluster, and ECR repo separately or extend this module.

Steps:
1. Set variables in `variables.tf` or via `-var` flags.
2. `terraform init`
3. `terraform plan`
4. `terraform apply`
