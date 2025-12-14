output "alb_dns_name" {
  description = "ALB DNS name to access the app"
  value       = aws_lb.alb.dns_name
}

output "ecs_cluster" {
  value = aws_ecs_cluster.this.id
}
