resource "aws_lambda_function" "scraper_telegram_bot" {
  description      = "A Wiesn availablity crawler"
  function_name    = var.lambda_name
  handler          = "main.lambda_handler"
  layers           = [aws_lambda_layer_version.python_packages.arn]
  memory_size      = 128
  package_type     = "Zip"
  role             = aws_iam_role.lambda.arn
  runtime          = "python3.8"
  filename         = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256
  architectures    = ["arm64"]

  tags = {
    "Owner" = "terraform"
  }

  timeout = 60

  timeouts {}

  tracing_config {
    mode = "PassThrough"
  }

  environment {
    variables = {
      TELEGRAM_TOKEN   = var.telegram_token,
      TELEGRAM_CHANNEL = var.telegram_channel,
      DESIRED_TIMES    = var.desired_times,
      DESIRED_DAYS     = var.desired_days,
      BUCKET_NAME      = aws_s3_bucket.data.id,
      SESSION_STORAGE  = "/tmp/vacancies.json",
      PYTHON_LOGLEVEL  = "INFO"
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.lambda
  ]
}

resource "aws_lambda_layer_version" "python_packages" {
  filename   = "./deployment/python.zip"
  layer_name = "python_packages"

  # if the no dependency package exists, force creation with a timestamp, that is always different
  source_code_hash = fileexists("./deployment/python.zip") ? filebase64sha256("./deployment/python.zip") : "${timestamp()}"

  compatible_runtimes = ["python3.8"]

  depends_on = [
    null_resource.create_dependencies_package
  ]
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_lambda" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.scraper_telegram_bot.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.cron_scheduler.arn
}

data "aws_region" "current" {}
