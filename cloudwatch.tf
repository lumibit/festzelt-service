resource "aws_cloudwatch_log_group" "lambda" {
  name = "/aws/lambda/${var.lambda_name}"

  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group
  # Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0.
  retention_in_days = 3
}
