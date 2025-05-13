# 🔒 inye-security-playground

**inye-security-playground**는 FastAPI 기반으로 구성된 웹 애플리케이션 보안 실습 프로젝트입니다.  
OWASP Top 10을 비롯한 다양한 보안 시나리오를 직접 구성하고 실험하는 것을 목적으로 합니다.

## 🎯 프로젝트 목적

- OWASP 기반 보안 위협 요소 실습 (Broken Authentication, Injection, XSS 등)
- JWT 기반 인증 구조와 그 취약점 실험
- Cloudflare Access, TLS, reverse proxy 등을 활용한 실전형 보안 환경 구성
- Stateless 인증 및 보안 설계 패턴에 대한 실험과 검증

## 🧪 주요 실험 항목 (예정)

- Broken Authentication: JWT alg=none 공격, 만료 우회 실험 등
- Broken Access Control: 역할 우회, 라우트 보호 실패 케이스 실험
- Injection: SQL Injection, 코드 인젝션 실험 등
- XSS: Stored/Reflected XSS 실험
- Misconfiguration: 디버그 모드, 노출된 Swagger, 미설정된 CORS 등

## 🧱 현재 구성

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

## 🚧 개발 노트
- 현재는 DB 없이 진행하며, 필요에 따라 추후 도입 예정
- 로그인 기능은 JWT 기반 stateless 방식으로 구성
- Cloudflare Access를 통해 외부 인증 게이트가 선행됨

## ⚠️ 경고
이 저장소는 보안 취약점 실험을 위한 목적으로 만들어졌으며, 실서비스에 사용하면 안 됩니다.
의도적으로 불안전한 코드가 포함될 수 있습니다.