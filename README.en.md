# 🔒 inye-security-playground

**inye-security-playground** is a FastAPI-based security testing project.  
It is designed to experiment with real-world security vulnerabilities such as those listed in the OWASP Top 10, and to simulate common insecure design patterns found in modern web applications.

## 🎯 Project Goals

- Explore and test OWASP Top 10 vulnerabilities (e.g., Broken Authentication, Injection, XSS)
- Analyze stateless authentication using JWT and its common pitfalls
- Build a real-world-like security environment using Cloudflare Access, TLS, and reverse proxies
- Study design-level security failures and validate secure architecture patterns

## 🧪 Planned Security Scenarios

- **Broken Authentication**: JWT `alg=none` attack, token expiry bypass
- **Broken Access Control**: role tampering, endpoint exposure
- **Injection**: SQL injection, code injection in unsafe eval scenarios
- **XSS**: stored and reflected cross-site scripting
- **Security Misconfiguration**: debug mode, exposed API docs, missing headers

## 🧱 Project Structure (WIP)

```text
my-fastapi-test/
├── app/
│   ├── core/          # 보안 유틸 (JWT 등)
│   ├── routes/        # API 라우트
│   ├── templates/     # Jinja2 템플릿
│   ├── static/        # 정적 파일
│   └── main.py        # 앱 진입점
├── gunicorn.conf.py
├── requirements.txt
└── README.md
```

## 🚧 Development Notes

- The app is currently database-free. Database support will be added as needed during development.
- Authentication is implemented using stateless JWT tokens.
- External access is gated through Cloudflare Access to simulate a zero-trust perimeter.

## ⚠️ Disclaimer

This project is intended for educational and security research purposes only.  
It may contain intentionally insecure code and **must not be used in production environments**.
