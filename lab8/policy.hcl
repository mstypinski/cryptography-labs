# Full access to secret paths with exceptions
path "secret/*" {
  capabilities = ["create", "read", "update", "patch", "delete", "list", "scan"]
}

# Explicit deny overrides broader rules
path "secret/super-secret" {
  capabilities = ["deny"]
}