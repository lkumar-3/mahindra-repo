variable "region" { type = string, default = "ap-south-1" }
variable "ecr_repo" { type = string }
variable "image_tag" { type = string }
variable "db_url" { type = string }
variable "task_exec_role_arn" { type = string }
variable "log_group" { type = string, default = "/ecs/orders" }
