# Cron Scheduling of Function Trigger
# https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-cron-expressions
# https://stackoverflow.com/a/35895316/5392813

resource "aws_cloudwatch_event_rule" "cron_scheduler" {
  name        = "${var.lambda_name}_lambda_scheduler"
  description = "Triggers Mo-Fr Run every 2 minutes 9-17"

  # Times in UTC!
  # https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
  schedule_expression = "cron(0/2 7-15 ? * 2-6 *)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  target_id = "${var.lambda_name}_lambda_scheduler"
  rule      = aws_cloudwatch_event_rule.cron_scheduler.name
  arn       = aws_lambda_function.scraper_telegram_bot.arn

}
