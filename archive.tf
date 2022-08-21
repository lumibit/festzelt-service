# https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/archive_file
data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "./src"
  output_path = "./deployment/deployment.zip"
  excludes    = ["__pycache__"]
}

#https://medium.com/rockedscience/hard-lessons-from-deploying-lambda-functions-with-terraform-4b4f98b8fc39
resource "null_resource" "create_dependencies_package" {
  provisioner "local-exec" {
    command = <<EOF
    docker build -f "Dockerfile" -t lambdalayer:latest . && \
    docker create --name lambdalayer lambdalayer:latest && \
    docker cp lambdalayer:/python.zip ./deployment/ ; \
    wait & \ 
    docker rm lambdalayer
    EOF
  }

  triggers = {
    dependencies_versions = filemd5("./src/requirements.txt")
    # always_run = "${timestamp()}"
  }
}
