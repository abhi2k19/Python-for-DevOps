# Launch Templates for Node Groups
resource "aws_launch_template" "eks_node" {
  for_each = var.node_groups
  
  name = "${var.cluster_name}-${each.key}-template"

  block_device_mappings {
    device_name = "/dev/xvda"

    ebs {
      volume_size           = lookup(each.value, "disk_size", 20)
      volume_type          = "gp3"
      encrypted           = true
      delete_on_termination = true
    }
  }

  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required"
    http_put_response_hop_limit = 2
  }

  monitoring {
    enabled = true
  }

  tag_specifications {
    resource_type = "instance"
    tags = merge(
      var.tags,
      {
        Environment = var.environment
        NodeGroup  = each.key
      }
    )
  }
}