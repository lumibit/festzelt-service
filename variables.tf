variable "lambda_name" {
  type        = string
  description = "AWS Lambda Function Name"
}

variable "aws_account" {
  type        = string
  description = "AWS Account for Deployment"
}

variable "telegram_token" {
  type        = string
  description = "The Bot token used to post to a telegram channel"
}

variable "telegram_channel" {
  type        = string
  description = "The Telegram Channel, the bot should post new tent vacancies"
}

variable "desired_times" {
  type        = string
  default     = "Mittag, Nachmittag"
  description = "The Times you want to go to Oktoberfest - Mittag, Nachmittag"
}

variable "desired_days" {
  type        = string
  default     = "Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag"
  description = "The Days you want to go to Oktoberfest - Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag"
}

variable "desired_seating_schottenhamel" {
  type        = string
  default     = "*"
  description = "The seating you want in Schottenhamel Tent - Halle, Hallenboxe, *, ..."
}

variable "desired_seating_schuetzenzelt" {
  type        = string
  default     = "*"
  description = "The seating you want in Schuetzen Tent - Reihe, Wiessee Box, *, ..."
}

