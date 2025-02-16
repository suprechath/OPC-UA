server.set_security_policy([
    ua.SecurityPolicyType.NoSecurity,  # No security (for testing)
    ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt  # Secure
])
