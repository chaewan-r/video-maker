# 독립 호스팅 가이드 (GitHub Pages)

## 1단계: GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단 `+` 버튼 → `New repository` 클릭
3. Repository name: `video-maker` (원하는 이름)
4. Public으로 설정 (GitHub Pages는 Public 저장소에서 무료)
5. `Create repository` 클릭

## 2단계: 코드를 GitHub에 푸시

```bash
# GitHub에서 알려주는 원격 저장소 URL을 추가
git remote add origin https://github.com/YOUR_USERNAME/video-maker.git

# 코드 푸시
git push -u origin main
```

## 3단계: GitHub Pages 활성화

1. GitHub 저장소 페이지에서 `Settings` 탭 클릭
2. 왼쪽 메뉴에서 `Pages` 클릭
3. Source 섹션에서:
   - Branch: `main` 선택
   - Folder: `/ (root)` 선택
4. `Save` 버튼 클릭
5. 몇 분 후 페이지 상단에 URL이 표시됨:
   `https://YOUR_USERNAME.github.io/video-maker/`

## 4단계: CORS 헤더 설정 (중요!)

GitHub Pages는 기본적으로 필요한 CORS 헤더를 제공하지 않습니다. 다음 중 하나를 선택하세요:

### 옵션 A: Cloudflare Pages 사용 (권장)

GitHub Pages 대신 Cloudflare Pages를 사용하면 CORS 헤더 설정이 쉽습니다:

1. [Cloudflare Pages](https://pages.cloudflare.com/)에 가입
2. `Create a project` 클릭
3. GitHub 계정 연결
4. 저장소 선택 (`video-maker`)
5. Build settings:
   - Framework preset: None
   - Build command: (비워둠)
   - Build output directory: `/`
6. `_headers` 파일이 자동으로 적용됨 (아래 참조)

### 옵션 B: Netlify 사용

1. [Netlify](https://www.netlify.com/)에 가입
2. `Add new site` → `Import an existing project`
3. GitHub 연결 및 저장소 선택
4. Deploy settings:
   - Build command: (비워둠)
   - Publish directory: `/`
5. `_headers` 파일이 자동으로 적용됨

## 5단계: _headers 파일 생성

Cloudflare Pages 또는 Netlify를 사용하는 경우, 프로젝트 루트에 `_headers` 파일을 생성하세요:

```bash
cat > _headers << 'EOF'
/standalone.html
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Embedder-Policy: require-corp
  Cross-Origin-Resource-Policy: cross-origin

/*
  Cross-Origin-Resource-Policy: cross-origin
EOF

git add _headers
git commit -m "CORS 헤더 추가"
git push
```

## 6단계: 접속 및 테스트

배포가 완료되면 (보통 1-2분 소요):

- **Cloudflare Pages**: `https://video-maker.pages.dev/standalone.html`
- **Netlify**: `https://your-site-name.netlify.app/standalone.html`
- **GitHub Pages**: `https://YOUR_USERNAME.github.io/video-maker/standalone.html`
  - ⚠️ GitHub Pages는 CORS 헤더 설정이 불가능하므로 FFmpeg.wasm가 작동하지 않을 수 있습니다

## 추천 호스팅 순위

1. **Cloudflare Pages** ✅ 무료, CORS 헤더 지원, 빠름
2. **Netlify** ✅ 무료, CORS 헤더 지원, 쉬운 설정
3. **GitHub Pages** ⚠️ 무료, 하지만 CORS 헤더 설정 불가

## 문제 해결

### "SharedArrayBuffer is not defined" 에러가 나는 경우

→ CORS 헤더가 제대로 설정되지 않았습니다. Cloudflare Pages나 Netlify를 사용하세요.

### 이미지가 업로드되지 않는 경우

→ 브라우저 콘솔(F12)을 열어 에러 메시지를 확인하세요.

### 동영상 생성이 실패하는 경우

→ 브라우저가 충분한 메모리를 가지고 있는지 확인하세요. Chrome이나 Edge를 사용하세요.

## Google Apps Script 버전

현재 `index.html`과 `javascript.html`은 Google Apps Script용으로 설정되어 있습니다.
독립 호스팅에서는 `standalone.html`을 사용하세요.
