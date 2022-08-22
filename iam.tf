
resource "aws_iam_role" "lambda" {
  name = "${var.lambda_name}_sts_role"
  assume_role_policy = jsonencode(
    {
      Statement = [
        {
          Action = "sts:AssumeRole"
          Effect = "Allow"
          Principal = {
            Service = "lambda.amazonaws.com"
          }
        },
      ]
      Version = "2012-10-17"
    }
  )
  force_detach_policies = false
  managed_policy_arns = [
    "${aws_iam_policy.lambda.arn}"
  ]
  max_session_duration = 3600
  path                 = "/service-role/"
  tags = {
    "Owner" = "terraform"
  }
}

resource "aws_iam_policy" "lambda" {
  name = "LambdaExecutionPolicy_${var.lambda_name}"
  path = "/service-role/"
  policy = jsonencode(
    {
      Statement = [
        {
          Action   = "logs:CreateLogGroup"
          Effect   = "Allow"
          Resource = "arn:aws:logs:${data.aws_region.current.name}:${var.aws_account}:*"
        },
        {
          Action = [
            "logs:CreateLogStream",
            "logs:PutLogEvents",
          ]
          Effect = "Allow"
          Resource = [
            "arn:aws:logs:${data.aws_region.current.name}:${var.aws_account}:log-group:/aws/lambda/${var.lambda_name}:*",
          ]
        },
        {
          Sid      = "ListObjectsInBucket"
          Action   = ["s3:ListBucket"]
          Effect   = "Allow"
          Resource = ["arn:aws:s3:::${aws_s3_bucket.data.bucket}"]
        },
        {
          Sid      = "AllObjectActions"
          Action   = "s3:*Object*"
          Effect   = "Allow"
          Resource = ["arn:aws:s3:::${aws_s3_bucket.data.bucket}/*"]
        }
      ]
      Version = "2012-10-17"
    }
  )
  tags = {
    "Owner" = "terraform"
  }
}
