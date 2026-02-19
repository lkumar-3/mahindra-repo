resource "aws_ecs_task_definition" "orders" {
  family                   = "orders"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = var.task_exec_role_arn
  container_definitions    = jsonencode([
    {
      name      = "orders"
      image     = "${var.ecr_repo}:${var.image_tag}"
      portMappings = [{ containerPort = 8080, protocol = "tcp" }]
      environment = [{ name = "DATABASE_URL", value = var.db_url }]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = var.log_group
          awslogs-region        = var.region
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}
