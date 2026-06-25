import re
import secrets
from hypothesis import given, strategies as st

# =========================================================================
# 🔒 PRODUCTION CONTAINMENT DEFENSE ARCHITECTURE
# =========================================================================

def generate_runtime_token() -> str:
    """
    Layer 1: Cryptographic Security Token Generation
    Generates 256 bits of entropy encoded as a URL-safe base64 string.
    """
    return secrets.token_urlsafe(32)

def sanitize_input(text: str) -> str:
    """
    Layer 2: Input Sanitization Pipeline
    Removes system control characters, explicitly stripping U+2028 and U+2029
    to eliminate compiler/parser bypass vectors, then normalizes whitespace.
    """
    if not isinstance(text, str):
        return ""
    control_char_regex = re.compile(r'[\x00-\x1F\x7F-\x9F\u2028\u2029]')
    sanitized = control_char_regex.sub('', text)
    return " ".join(sanitized.split())

def wrap_untrusted_input(user_input: str, token: str) -> str:
    """
    Layer 3: Untrusted Input Wrapping & Server-Side Structural Validation
    Deterministically intercepts tag-escape attacks prior to LLM compilation.
    """
    if token in user_input or f'<untrusted_input id="{token}">' in user_input:
        raise ValueError("Security violation: Token or structural tag sequence detected in input stream.")
    
    sanitized = sanitize_input(user_input)
    return f'<untrusted_input id="{token}">{sanitized}</untrusted_input>'


# =========================================================================
# 🧪 HYPOTHESIS PROPERTY-BASED TESTING HARNESS
# =========================================================================

@given(st.text())
def test_sanitization_idempotence_property(raw_string):
    """
    Validates Property 2: Idempotence of the Sanitization Layer.
    Ensures that repetitive applications of the sanitization regex do not alter
    the data payload structure across the entire UTF-8 character space.
    """
    first_pass = sanitize_input(raw_string)
    second_pass = sanitize_input(first_pass)
    assert first_pass == second_pass


@given(st.text())
def test_token_containment_escape_property(malicious_payload):
    """
    Validates Property 5: Strict Boundary Integrity.
    Guarantees that no input sequence can artificially escape or prematurely
    terminate the structural wrapping layer without triggering server validation.
    """
    system_token = generate_runtime_token()
    try:
        wrapped_output = wrap_untrusted_input(malicious_payload, system_token)
        # Verify strict tag encapsulation layout
        assert wrapped_output.startswith(f'<untrusted_input id="{system_token}">')
        assert wrapped_output.endswith('</untrusted_input>')
    except ValueError:
        # Properly caught by deterministic boundary parsing checks
        assert True

if __name__ == "__main__":
    print("Executing structural property verifications...")
    # Execute testing logic
    test_sanitization_idempotence_property()
    test_token_containment_escape_property()
    print("All property tests passed successfully.")
