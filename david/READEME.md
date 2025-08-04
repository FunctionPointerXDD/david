
### ✅ Personal Access Token을 텍스트 파일로 저장한 뒤 삭제해야 하는 이유

**이유**:

| 항목              | 설명                                                         |
| --------------- | ---------------------------------------------------------- |
| 🔒 민감정보         | PAT는 계정에 대한 **인증 수단**으로, 유출 시 원격에서 푸시/삭제 등 위험 가능           |
| 🔍 GitHub 자동 탐지 | GitHub는 공개 저장소에서 **토큰 문자열을 자동으로 감지**하여 사용자에게 경고함           |
| 📁 평문 파일 위험     | 텍스트 파일은 암호화되지 않으며, 백업/버전관리 도구에 실수로 포함될 수 있음                |
| ✅ 안전한 인증 절차     | 사용 후 텍스트 파일은 반드시 삭제하고 **자격증명 도구(GCM)** 나 **Keyring** 사용 권장 |

**보안 습관**:

* 토큰은 `.env`, `.gitignore`, `.bashrc` 등에서 관리
* 노출된 경우 GitHub에서 즉시 토큰 **Revoke** 해야 함

---

## 🧹 문제 3: Python 프로젝트에서 .gitignore 사용 이유

### ✅ `__pycache__`, `.venv` 디렉토리 생성 이유

| 디렉토리          | 역할                                                |
| ------------- | ------------------------------------------------- |
| `__pycache__` | Python이 `.py` 파일을 `.pyc`로 컴파일해 저장하는 디렉토리 (성능 최적화) |
| `.venv`       | 가상환경 디렉토리, 프로젝트마다 독립된 Python 패키지 관리 공간            |

→ **공통점**: **자동 생성되며 Git에 포함할 필요 없음**

---

### ✅ `.gitignore`에 포함시키는 이유

* 자동 생성 파일 또는 **환경별로 달라지는 파일**은 Git 관리에서 제외
* 협업 시 깨끗한 환경 유지 가능
* 가상환경, OS별 파일, IDE 설정 등을 포함하지 않음

---

### ✅  GitHub에서 Python `.gitignore` 템플릿 포함 항목 확인

링크: [https://github.com/github/gitignore/blob/main/Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

주요 포함 항목:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
env/
venv/

# Distribution / packaging
*.egg-info/
dist/
build/

# IDE settings
.vscode/
.idea/
```

---

### ✅ 3-4. Flask 프로젝트 기준 `.gitignore`에 추가할 항목 예시

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual Envs
.venv/
env/
venv/

# Flask instance/config files
instance/
*.env
.env.*

# Static/Generated
*.log
*.sqlite3
*.db

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## 📦 정리

| 항목       | 핵심 내용                                               |
| -------- | --------------------------------------------------- |
| **문제 1** | 오픈소스 Fork → 토큰은 민감 정보로 저장 후 반드시 삭제                  |
| **문제 2** | `git clone`으로 PC/디렉토리 어디서든 복제 가능                    |
| **문제 3** | `.gitignore`는 Python 프로젝트의 캐시/가상환경/IDE 설정 제거를 위해 필수 |

---

