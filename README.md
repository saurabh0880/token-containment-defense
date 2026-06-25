[![Security Property Verification](https://github.com)](https://github.com)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Security: Property-Based Verification](https://shields.io)](https://github.com)

# Token-Based Containment Defense Against Prompt Injection


This repository contains the official open-source code implementation and property-based evaluation engine for **"Containment over Detection: A Token-Based Defense Against Prompt Injection in Production Agentic Systems with Property-Based Validation"**.

## 🚀 Performance & Core Metrics
Unlike fragile, high-latency detection guardrails (semantic classifiers or keyword filters), this architecture shifts security boundaries from inference compliance to deterministic, server-side string encapsulation.

* **Block Rate:** 94% against advanced injection vectors (OWASP LLM Top 10 & Garak Prompt Probes).
* **Latency Overhead:** <0.5ms synchronous pipeline execution time (compared to 180ms text classification pipelines).
* **False Positive Rate:** 0.0% across real-world enterprise production message distributions.

---

## 🏛️ System Architecture
The defense strategy operates as a rigid 4-Layer synchronous sandwich:
1. **Cryptographic Token Layer:** Generates high-entropy random sequence flags (`secrets.token_urlsafe(32)`) at container boot.
2. **Sanitization Filtering:** Strips compiler bypass tokens, specifically capturing multi-stage sequence gaps (`U+2028` and `U+2029`).
3. **Envelope Wrapping Layer:** Encapsulates raw untrusted strings within XML tag boundaries linked deterministically to the active container session token.
4. **Instruction Directives:** Instructs the downstream LLM processing engine to treat the bounded block as static string literals.

---

## 🔧 Installation & Automated Validation

Execute the property-based testing suites locally using the following steps:

```bash
# Clone the repository
git clone https://github.com/token-containment-defense.git
cd token-containment-defense

# Install validation requirements
pip install hypothesis

# Execute the property verification test harness
python main.py
```

## 🧪 Property-Based Verification Layout
We declare 15 architectural invariants verified across thousands of adversarial input combinations generated via the `Hypothesis` framework:

| Property Category | Strategy Invariants Measured | System Status |
| :--- | :--- | :--- |
| **Security** | Token Uniqueness & Base Entropy Evaluation | `PASSED` |
| **Security** | Sanitization Idempotence Strategy Bounds | `PASSED` |
| **Security** | Server-Side Structural Tag-Escape Interception | `PASSED` |
| **Observability** | Contextvar Propagation & Non-Blocking Buffer Drops | `PASSED` |

---

## 📝 Citation Tracking & Academic Indexing
If you use this containment baseline or the property-based testing harness in your security research, please cite the preprint reference layout:

```bibtex
@article{sharma2026containment,
  title={Containment over Detection: A Token-Based Defense Against Prompt Injection in Production Agentic Systems with Property-Based Validation},
  author={Sharma, Saurabh and Authors, Anonymous},
  journal={arXiv preprint},
  url={https://github.com/saurabh0880/token-containment-defense},
  year={2026}
}

```
