# Weather App

This is a simple static weather app built with HTML and deployed as part of my AWS cloud practice.

## Cloud Deployment Practice

I used this project to practice deploying a static website in two different ways:

- Hosted on an AWS EC2 instance using Apache/httpd
- Uploaded to an Amazon S3 bucket for static website hosting practice

## What I Practiced

- Git and GitHub project tracking
- Static website hosting
- AWS EC2
- Apache/httpd
- Amazon S3
- Comparing EC2 hosting vs S3 static hosting

## Files

- `index.html` - Main weather app file
- `weather-icon.png` - Weather app image asset

## CI/CD Deployment

This project uses GitHub Actions to automatically deploy the static website to an AWS S3 bucket whenever changes are pushed to the `main` branch.

### Workflow

1. Code is pushed to GitHub
2. GitHub Actions runs the deployment workflow
3. AWS credentials are loaded from GitHub Secrets
4. The project files are synced to the S3 bucket
5. The static website updates automatically

### Tools Used

- GitHub Actions
- YAML
- AWS S3
- GitHub Secrets
- AWS CLI