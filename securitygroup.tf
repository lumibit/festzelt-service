resource "aws_security_group" "lambda" {
  name        = "${var.lambda_name}-lambda"
  description = "Traffic Security for Lambda and EFS"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "${var.lambda_name}-lambda"
    "Owner" = "terraform"

  }
}
