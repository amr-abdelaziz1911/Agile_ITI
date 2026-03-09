# Agile Software Development — Clean Code & TDD

> Course task implementing clean code principles and Test Driven Development techniques in Python.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Task 1 — Sum of Integers in a String](#task-1--sum-of-integers-in-a-string)
   - [Clean Code Principles Applied](#clean-code-principles-applied)
   - [How to Run](#how-to-run)
3. [CI/CD Pipeline Benchmark](#cicd-pipeline-benchmark)
   - [When to Use](#when-to-use)
   - [Pricing](#pricing)
   - [Quick Verdict](#quick-verdict)

---

## Project Overview

This project is part of an agile software development course focused on writing readable, maintainable, and testable code. It covers:

- **Clean Code** — meaningful naming, single responsibility, guard clauses, and no magic values
- **Test Driven Development (TDD)** — writing tests before implementation following the Red → Green → Refactor cycle

**Stack:** Python 3.10+ · pytest

---


### Clean Code Principles Applied

| Principle | How it's applied |
|---|---|
| **Single Responsibility** | `extract_integers()` only extracts — `sum_integers_in_string()` only sums |
| **Meaningful Names** | No `x`, `s`, or `tmp` — every name describes its intent |
| **Type Hints** | Input/output contract is explicit and machine-checkable |
| **Guard Clause** | `TypeError` raised early before any logic runs |
| **Docstring** | Describes args, return value, exceptions, and examples |
| **No Magic Values** | Regex `-?\d+` is in a dedicated extraction function, not buried inline |

---

### How to Run

```bash
# Install dependencies
pip install unittest

# Run the function manually
python string_sum.py

# Run the test suite
pytest test_string_sum.py -v
```

---

## CI/CD Pipeline Benchmark

Comparison of **Jenkins**, **AWS CodePipeline**, and **GitHub Actions** for integrating CI into this project and similar Python/agile workflows.

---

### When to Use

#### 🏗️ Jenkins

**Use when:**
- You need full on-premises or air-gapped deployment
- Your pipelines are complex and require deep customization
- You have a dedicated DevOps team to manage infrastructure and plugins

**Avoid when:**
- Your team lacks ops capacity — maintenance overhead is significant
- You need fast, zero-config CI setup

#### ☁️ AWS CodePipeline

**Use when:**
- You deploy exclusively to AWS (ECS, EKS, Lambda, Beanstalk)
- You need native IAM, VPC, and CloudWatch integration out of the box
- You're under compliance frameworks (SOC 2, HIPAA) needing AWS audit trails

**Avoid when:**
- You deploy to multiple clouds or on-prem targets
- You need rich third-party integrations outside the AWS ecosystem

#### ⚙️ GitHub Actions

**Use when:**
- Your source code is already on GitHub — zero friction, native integration
- You need fast CI/CD without managing any infrastructure
- You maintain open-source projects (unlimited free minutes on public repos)

**Avoid when:**
- You have very high build volumes on private repos (minutes cost adds up)
- Your source code cannot be hosted on GitHub

---

### Pricing

| Dimension | 🏗️ Jenkins | ☁️ AWS CodePipeline | ⚙️ GitHub Actions |
|---|---|---|---|
| **Base cost** | Free (OSS) | `$1.00/month` per active pipeline | Free for public repos |
| **Compute** | You pay for your own servers | CodeBuild: ~`$0.005/min` | Linux `$0.008/min` · macOS `$0.08/min` |
| **Free tier** | Unlimited (you own the infra) | 1 free pipeline/month | 2,000 min/month (Free plan) |
| **Storage** | Your own disk | S3 rates | 500 MB free, then `$0.25/GB/month` |
| **Hidden costs** | Ops/maintenance labor — often `$5K–$50K/yr` | CloudWatch, KMS, data transfer fees | Matrix builds drain minutes fast |
| **TCO (small team)** | `$200–800/month` | `$50–300/month` | `$0–50/month` |

---



### Quick Verdict

| | 🏗️ Jenkins | ☁️ AWS CodePipeline | ⚙️ GitHub Actions |
|---|---|---|---|
| **Best for** | Complex enterprise, on-prem | AWS-only deployments | Most teams, OSS, multi-cloud |
| **Operational overhead** | High | None | Low |
| **Setup time** | Days–Weeks | Hours | Minutes |
| **Cost (small team)** | Medium–High | Low–Medium | Low |
| **Ecosystem** | 1,800+ plugins | AWS services | 10,000+ actions |



- Choose **Jenkins** if you need maximum control and have the team to manage it.
- Choose **AWS CodePipeline** if you're all-in on AWS and want zero maintenance.
- Choose **GitHub Actions** for this course project and most agile team setups — fastest setup, best developer experience, lowest cost.

---

*Collected and made by:*
- Moustafa Mamdouh
- Marwan Tamer
- Amr Abdelaziz
- Mazen Mohamed
- Mahmoud Abdeltawab Saqr
