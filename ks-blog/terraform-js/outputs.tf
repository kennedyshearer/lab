output "cloudfront_distribution_id" {
  value       = aws_cloudfront_distribution.website_distribution.id
  description = "CloudFront distribution ID, useful for cache invalidations"
}

output "cloudfront_url" {
  value = aws_cloudfront_distribution.website_distribution.domain_name
  description = "CloudFront distribution URL"
}

output "s3_bucket_regional_domain_name" {
  value       = aws_s3_bucket.website.bucket_regional_domain_name
  description = "S3 REST endpoint used as the CloudFront origin"
}